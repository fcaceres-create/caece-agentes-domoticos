# Agentes inteligentes en entornos domóticos

Implementación en Python de dos arquitecturas de agentes para el control 
de un sistema de calefacción inteligente. Actividad N°1 - Unidad Temática III 
de la Maestría en Gestión y Desarrollo de IA (CAECE).

## Objetivo

Comprender la diferencia práctica entre un **Agente Reactivo Simple** y un 
**Agente Reactivo Basado en Modelos** mediante la programación de sus lógicas 
de decisión.

## Escenario

Sistema de calefacción inteligente (Softbot) en una casa con losa radiante.

- **Sensores**: temperatura actual y estado de ventanas (abiertas/cerradas).
- **Actuadores**: encendido/apagado de los relés de calefacción.

## Agentes implementados

### Agente Reactivo Simple
Decide únicamente en base a la temperatura actual, ignorando el resto de las 
variables del entorno.

- Temperatura < 19°C → ENCENDER
- Temperatura > 21°C → APAGAR
- Entre 19°C y 21°C → NINGUNA

### Agente Basado en Modelo
Mantiene un estado interno sobre el entorno (estado de la ventana) y 
combina esa información con la percepción actual.

- Si hace frío pero la ventana está abierta, no enciende la calefacción 
  para evitar desperdicio de energía.
- En el resto de los casos, replica la lógica del agente simple.

## Resultado de la simulación

Con temperatura = 17°C y ventana abierta:

| Agente | Acción tomada |
|---|---|
| Reactivo Simple | ENCIENDE la calefacción (ineficiente) |
| Basado en Modelo | NO enciende (detecta ventana abierta) |

## Ejecución

```bash
python agentes_domoticos.py
```

## Tecnologías

Python (sin dependencias externas)
