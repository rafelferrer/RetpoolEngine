# Retpool Engine 🐦🎮

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Pygame](https://img.shields.io/badge/Pygame-2.6.1-green) ![License](https://img.shields.io/badge/License-MIT-lightgrey)

**Retpool Engine** es un motor 2D modular en Python para crear juegos sencillos tipo Flappy Bird, Pac-Man o Buscaminas.  
Creado por **Rafel Ferrer Gomà (Lupter)** con ayuda de **ChatGPT** 🤖.

![Flappy Bird Demo](assets/flappy_demo.gif)

---

## 🛠 Características

- 🖥 Ventana y loop principal configurable  
- 🎨 Sistema de escenas/pantallas (menú, juego, game over)  
- 🕹 Sprites animados y sprites estáticos  
- 💥 Detección de colisiones simple  
- ⌨️ Input de teclado y ratón  
- 🧩 Modular: añadir nuevos juegos fácilmente  
- 🐦 Ejemplo incluido: **Flappy Bird** funcional

---

## 📂 Estructura del proyecto

```
RetpoolEngine/
├─ engine/               # Código del motor
│   ├─ __init__.py
│   ├─ window.py
│   ├─ scene.py
│   ├─ sprite.py
│   └─ collision.py
├─ games/                # Juegos creados con el motor
│   └─ flappy_bird/
│       └─ main.py
├─ assets/               # Sprites, sonidos y gifs
└─ README.md
```

---

## 🚀 Cómo ejecutar

1. Instala **Python 3.10+** y **Pygame**:

```bash
sudo pacman -S python-pip    # si no tienes pip
pip install pygame
```

2. Sitúate en la carpeta raíz:

```bash
cd ruta/a/RetpoolEngine
```

3. Ejecuta el juego:

```bash
python -m games.flappy_bird.main
```

> En Hyprland/Wayland, si falla la ventana:

```bash
export SDL_VIDEODRIVER=wayland
python -m games.flappy_bird.main
```

- **Controles**: Espacio → saltar / reiniciar juego tras Game Over

---

## 🖌 Cómo crear tu propio juego

1. Crear carpeta dentro de `games/` con el nombre de tu juego  
2. Crear `main.py` y usar Retpool Engine:

```python
from engine.window import Window
from engine.scene import Scene
from engine.sprite import Sprite
```

3. Crear escenas (`Scene`) y añadir sprites.  
4. Ejecutar el loop principal:

```python
window = Window(width, height, "Mi Juego")
scene = MiEscena()
window.run(scene)
```

---

## 🎉 Extras recomendados

- Añadir animaciones a tus sprites  
- Crear menú y pantalla de Game Over personalizados  
- Guardar puntuaciones en un archivo `.txt` o `.json`  
- Añadir más mini juegos usando Retpool Engine

---

## 📜 Licencia

Open Source. Puedes usar Retpool Engine para crear tus propios juegos y aprender Python/Pygame.