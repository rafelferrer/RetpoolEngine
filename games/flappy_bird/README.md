# Flappy Bird - Retpool Engine 🐦

**Flappy Bird** es un mini juego hecho con **Retpool Engine**, creado por **Rafel Ferrer Gomà (Lupter)** con la ayuda de **ChatGPT** 🤖.

![Flappy Bird Demo](assets/flappy_demo.gif)

---

## 🛠 Características

- 🐤 Pájaro amarillo que salta al pulsar espacio
- 🟩 Pipes verdes que se mueven hacia la izquierda
- 💥 Detección de colisiones con pipes y suelo/techo
- 🏆 Score funcional que aumenta cada vez que el pájaro pasa una tubería
- 🔄 Reinicio automático tras Game Over

---

## 📂 Estructura del juego

```
games/flappy_bird/
├─ main.py        # Script principal para ejecutar el juego
└─ assets/        # (Opcional) sprites o gifs si los añades
```

---

## 🚀 Cómo jugar

1. Ejecuta el juego desde la raíz de Retpool Engine:

```bash
python -m games.flappy_bird.main
```

> En Hyprland/Wayland, si la ventana no aparece:

```bash
export SDL_VIDEODRIVER=wayland
python -m games.flappy_bird.main
```

- **Controles:** Espacio →