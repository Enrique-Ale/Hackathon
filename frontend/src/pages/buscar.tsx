import React from "react";

export default function Buscar() {
  return (
    <div className="min-h-screen bg-gray-50 p-4">
      <header className="mb-6">
        <h1 className="text-3xl font-bold text-gray-800">Buscar Proveedores</h1>
      </header>
      <div className="bg-white p-6 rounded-xl shadow-md">
        <h2 className="text-xl font-semibold mb-4">Filtros</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <input placeholder="Oficio" className="border p-2 rounded-lg" />
          <input placeholder="Zona" className="border p-2 rounded-lg" />
          <select className="border p-2 rounded-lg">
            <option>Disponibilidad</option>
            <option>Disponible</option>
          </select>
        </div>
      </div>
      <div className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white p-6 rounded-xl shadow-md">
          <h3 className="font-bold text-lg">Juan Pérez</h3>
          <p className="text-gray-500">Plomería · Coyoacán</p>
          <p className="mt-2 text-sm">Reputación: ⭐ 4.8</p>
          <button className="mt-4 w-full bg-blue-600 text-white py-2 rounded-lg">Seleccionar</button>
        </div>
        <div className="bg-white p-6 rounded-xl shadow-md">
          <h3 className="font-bold text-lg">María García</h3>
          <p className="text-gray-500">Electricidad · Naucalpan</p>
          <p className="mt-2 text-sm">Reputación: ⭐ 4.9</p>
          <button className="mt-4 w-full bg-blue-600 text-white py-2 rounded-lg">Seleccionar</button>
        </div>
      </div>
    </div>
  );
}

