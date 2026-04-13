from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Literal
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./banco_local.db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class RegistroCashback(Base):
    __tablename__ = "historico_cashback"
    id = Column(Integer, primary_key=True, index=True)
    ip_usuario = Column(String)
    tipo_cliente = Column(String)
    valor_compra = Column(Float)
    cashback_resultado = Column(Float)

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

def calcular_cashback(valor_compra: float, desconto_percentual: float, vip: bool) -> float:
    valor_final = valor_compra * (1 - desconto_percentual / 100)
    cashback_base = valor_final * 0.05

    if valor_final > 500:      
        cashback_base *= 2

    bonus_vip = cashback_base * 0.10 if vip else 0.0
    return round(cashback_base + bonus_vip, 2)

class CashbackSchema(BaseModel):
    valor: float
    tipo: Literal["normal", "vip"] 
    desconto: float = 0.0

@app.post("/calcular")
async def calcular_e_salvar(dados: CashbackSchema, request: Request):
    client_ip = request.headers.get("x-forwarded-for", request.client.host).split(",")[0].strip() 
    resultado = calcular_cashback(dados.valor, dados.desconto, dados.tipo == "vip")

    with SessionLocal() as db:  
        db.add(RegistroCashback(
            ip_usuario=client_ip,
            tipo_cliente=dados.tipo,
            valor_compra=dados.valor,
            cashback_resultado=resultado,
        ))
        db.commit()

    return {"cashback": resultado}

@app.get("/historico")
async def buscar_historico(request: Request):
    client_ip = request.headers.get("x-forwarded-for", request.client.host).split(",")[0].strip()
    with SessionLocal() as db:
        logs = db.query(RegistroCashback).filter(RegistroCashback.ip_usuario == client_ip).all()
    return logs