# Fedele Tunnels Extension
Esta extension es un fork de https://github.com/robertlynch3/netbox-tunnels2

## Creación del Fork
Para futuras actualizaciones de la Extensión, si se desea realizar un nuevo fork, se debe realizar el siguiente procedimiento:

1. Hacer el Fork
2. Añadir remoto: 
  
  ```
  git remote add upstream [GitHub repo original]
  ```

3. Obtener tags: 
  ```
  git fetch upstream --tags
  ```

4. Ir a rama main:
  ```
  git checkout main
  ```

5. Reiniciar rama main con el tag a utilizar:

  ```
  git reset --hard tags/nombre-del-tag  
  ```

6. Pushear cambios:
  ```
  git push --force origin main
  ```

## Instalación

1. Cambiar netbox_dns por fedele_dns en ```__init__.py``` y en ```setup.py```

2. Cambiar nombre de carpeta de proyecto a ```fedele_dns```

3. Cambiar nombre de carpeta ```/fedele_dns/templates/netbox_dns``` a ```/fedele_dns/templates/fedele_dns```

4. Con ```Ctrl + Shift + H``` reemplazar ```netbox_dns``` por ```fedele_dns``` en TODOS lados. 
    
    * [IMPORTANTE] Activar Match Whole Word (Palabra exacta). Caso contrario se van a reemplazar variables no deseadas y no va a funcionar correctamente.

5. Con ```Ctrl + Shift + H``` reemplazar ```netbox-dns``` por ```fedele-dns``` en TODOS lados.
    * [IMPORTANTE] Probar si funciona SIN este paso, caso contrario, realizarlo.

6. Activar entorno virtual: 
```
source /opt/o4n/O4N_FEDELE_SOURCE/venv/bin/activate
```

7. Instalar Extensión: 
  ```
  python setup.py develop
  ```

8. En ```configuration.py``` de Fedele agregar:
  ```
  PLUGINS = ["fedele_dns"]
  ```

9. Eliminar todas las migraciones de la carpeta ```migrations```

10. Detectar migraciones:
  ```
  python manage.py makemigrations
  ```

11. Ejecutar migraciones:
  ```
  python manage.py migrate
  ```

Nota: En caso de que no se ejecuten las migraciones, ejecutar el siguiente comando para anularlas:
```
python manage.py migrate fedele_dns zero --fake
```

Y luego volver a ejecutar:
```
python manage.py migrate fedele_dns
```