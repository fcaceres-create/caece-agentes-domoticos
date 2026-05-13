# =============================================================================
# Actividad N° 1 - Agentes inteligentes en entornos domóticos
# Comparación entre Agente Reactivo Simple y Agente Basado en Modelos
# =============================================================================

class EntornoSmartHome:
    def __init__(self, temp_inicial, ventana_abierta):
        self.temperatura = temp_inicial
        self.ventana_abierta = ventana_abierta
        self.calefaccion_encendida = False

    def obtener_percepcion(self):
        # Devuelve la percepción actual del entorno
        return {"temperatura": self.temperatura, "ventana_abierta": self.ventana_abierta}

    def ejecutar_accion(self, accion):
        if accion == "ENCENDER_CALEFACCION":
            self.calefaccion_encendida = True
            print("Acción: Relés de calefacción ENCENDIDOS.")
        elif accion == "APAGAR_CALEFACCION":
            self.calefaccion_encendida = False
            print("Acción: Relés de calefacción APAGADOS.")
        else:
            print("Acción: NINGUNA (Standby).")


# --- CLASES DE AGENTES ---

class AgenteReactivoSimple:
    """
    Agente reactivo simple: aplica reglas de condición-acción basadas
    únicamente en la percepción actual de la temperatura.
    No tiene memoria ni considera otras variables del entorno.
    """
    def __init__(self):
        self.tipo = "Reactivo Simple"

    def actuar(self, percepcion):
        # Solo evalúa la variable 'temperatura', ignorando el resto.
        temperatura = percepcion["temperatura"]

        if temperatura < 19:
            return "ENCENDER_CALEFACCION"
        elif temperatura > 21:
            return "APAGAR_CALEFACCION"
        else:
            # Zona de confort (entre 19°C y 21°C): no actuar.
            return "NINGUNA"


class AgenteBasadoEnModelo:
    """
    Agente reactivo basado en modelos: mantiene un estado interno
    sobre el entorno (en este caso, si la ventana está abierta).
    Toma decisiones combinando la percepción actual con su modelo
    interno, evitando acciones ineficientes.
    """
    def __init__(self):
        self.tipo = "Basado en Modelo"
        # Estado interno: guardamos si sabemos que la ventana está abierta
        self.estado_interno_ventana = False

    def actualizar_estado(self, percepcion):
        self.estado_interno_ventana = percepcion["ventana_abierta"]

    def actuar(self, percepcion):
        # 1) Actualizar el estado interno a partir de la percepción.
        self.actualizar_estado(percepcion)

        temperatura = percepcion["temperatura"]

        # 2) Lógica que considera temperatura Y estado de la ventana.
        if temperatura < 19:
            # Si hace frío pero el modelo del entorno indica que la ventana
            # está abierta, no encender la calefacción para evitar el
            # desperdicio energético (el calor se escaparía).
            if self.estado_interno_ventana:
                print("Modelo interno: ventana abierta detectada. "
                      "Se evita encender la calefacción para no desperdiciar energía.")
                return "NINGUNA"
            else:
                return "ENCENDER_CALEFACCION"
        elif temperatura > 21:
            return "APAGAR_CALEFACCION"
        else:
            return "NINGUNA"


# --- SCRIPT DE PRUEBA ---
if __name__ == "__main__":
    print("--- Simulando Entorno: Hace frío y están ventilando (Ventana Abierta) ---")
    entorno = EntornoSmartHome(temp_inicial=17, ventana_abierta=True)
    percepcion_actual = entorno.obtener_percepcion()

    print("\nEvaluando Agente Reactivo Simple:")
    agente_simple = AgenteReactivoSimple()
    accion_simple = agente_simple.actuar(percepcion_actual)
    entorno.ejecutar_accion(accion_simple)

    print("\nEvaluando Agente Basado en Modelo:")
    agente_modelo = AgenteBasadoEnModelo()
    accion_modelo = agente_modelo.actuar(percepcion_actual)
    entorno.ejecutar_accion(accion_modelo)
