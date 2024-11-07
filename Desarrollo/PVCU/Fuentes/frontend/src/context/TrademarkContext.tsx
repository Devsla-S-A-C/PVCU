import { createContext, ReactNode, useState, useEffect } from "react";
import { Marca, Plan, Suscripcion } from "@/types";

const marcaData:Marca={
  id:"1",
  nombre: "marca1",
  logo: "logo1",
  descripcion: "descripcion1",
  facebook: "facebook1",
  instagram: "instagram1",
  tiktok: "tiktok1",
  otra_red_social: "red_social1",
  activado:false,
}
const planData:Plan={
  id: "1",
  tipo: "gratuito",
  duracion: "ilimitado",
  precio: 0,
}
const suscripcionData:Suscripcion={
  id:"1",
  usuario:"1",
  plan:"1",
  fecha_vencimiento:"22/12/2024",
}

interface TrademarkContextType {
  marca: Marca|null;
  setMarca: React.Dispatch<React.SetStateAction<Marca|null>>;
  suscripcion: Suscripcion;
  planActual: Plan;
  planSeleccionado: Plan|null;
  setPlanSeleccionado: React.Dispatch<React.SetStateAction<Plan|null>>;
}

export const TrademarkContext = createContext<TrademarkContextType | null>(null);

export const TrademarkProvider = ({ children }: { children: ReactNode }) => {
  
  const [marca, setMarca] = useState<Marca|null>(marcaData);
  const [suscripcion, setSuscripcion] = useState<Suscripcion>(suscripcionData);
  const [planActual, setPlanActual] = useState<Plan>(planData);
  const [planSeleccionado, setPlanSeleccionado] = useState<Plan|null>(null);

  useEffect(() => {
    //setMarca(get api from marca)
    //setPlanActual(get api from plan)
  }, []);

  return (
    <TrademarkContext.Provider value={{ marca, setMarca, suscripcion,planActual,  planSeleccionado, setPlanSeleccionado}}>
      {children}
    </TrademarkContext.Provider>
  );
}
