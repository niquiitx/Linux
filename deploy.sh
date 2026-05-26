#!/bin/bash

echo "Iniciamos el despliegue automatico de Don Alberto"

# moverse a la carpeta del proyecto
cd /home/$USER/moto-api

# traer los cambios desde git
echo "Trayendo la ultima version desde GitHub"
git pull origin master

# activar el entorno virtual
echo "Activando entorno virtual"
source venv/bin/activate

# instalar dependencias
echo "Instalando dependencias"
pip install -r requirements.txt

# reiniciar el servicio
echo "Reiniciando servicio Flask"
sudo systemctl restart gigamoto.service

# verificar estado
echo "Verificando estado del servicio"
sudo systemctl status gigamoto.service

echo "Despliegue completado correctamente"
