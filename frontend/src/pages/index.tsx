import React from "react";

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center justify-center p-4">
      <header className="mb-8 text-center">
        <h1 className="text-4xl font-bold text-blue-600 mb-2">Chamba Solidaria MX</h1>
        <p className="text-gray-600">Conectando oficios, servicios y comunidad.</p>
      </header>

      <main className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl w-full">
        <div className="bg-white p-8 rounded-xl shadow-md border border-gray-100 hover:shadow-lg transition-shadow cursor-pointer">
          <h2 className="text-2xl font-semibold text-gray-800 mb-4">Necesito un servicio</h2>
          <p className="text-gray-500 mb-6">Busca trabajadores calificados, colectivos o cooperativas en tu zona.</p>
          <button className="w-full bg-blue-600 text-white py-3 rounded-lg font-medium hover:bg-blue-700 transition-colors">
            Buscar Ayuda
          </button>
        </div>

        <div className="bg-white p-8 rounded-xl shadow-md border border-gray-100 hover:shadow-lg transition-shadow cursor-pointer">
          <h2 className="text-2xl font-semibold text-gray-800 mb-4">Ofrezco mis servicios</h2>
          <p className="text-gray-500 mb-6">Regístrate como trabajador independiente y ofrece tus habilidades.</p>
          <button className="w-full bg-green-600 text-white py-3 rounded-lg font-medium hover:bg-green-700 transition-colors">
            Registrarme
          </button>
        </div>
      </main>

      <footer className="mt-16 text-gray-400 text-sm">
        &copy; 2026 Chamba Solidaria MX - Economía Social y Solidaria
      </footer>
    </div>
  );
}

