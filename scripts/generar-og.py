"""Genera las imágenes Open Graph (1200x630) del curso.

Uso (desde la raíz del proyecto; Windows: `py`, Linux/macOS: `python3`):
    pip install pillow pyyaml
    py scripts/generar-og.py

Lee el frontmatter de src/content/modulos/*.md y escribe public/og/<archivo>.png,
más public/og/og-default.png para la landing. Cada PNG debe pesar < 300 KB.

Colores: copia de los tokens oscuros de src/styles/global.css. Si cambian allá,
actualiza COLORES aquí. Fuentes: se prueba cada ruta de la lista en orden
(Windows: Segoe UI y Consolas; Linux: Inter y DejaVu; macOS: Helvetica/Menlo).
Todas deben tener tildes y eñes. Variable de entorno OG_FUENTES_DIR opcional
para apuntar a una carpeta propia con los .ttf/.otf.
"""
from pathlib import Path
import sys

import yaml
from PIL import Image, ImageDraw, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
MODULOS = RAIZ / "src" / "content" / "modulos"
SALIDA = RAIZ / "public" / "og"

ANCHO, ALTO = 1200, 630
MARGEN = 72

def hexa(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


# Tokens oscuros de src/styles/global.css
COLORES = {
    "fondo": hexa("#1a1613"),        # --bg
    "fondo_borde": hexa("#2e2721"),  # --surface-2 (marco y número decorativo)
    "texto": hexa("#f3ebe1"),        # --text
    "suave": hexa("#bfb2a3"),        # --text-muted
    "acento": hexa("#ff8a3d"),       # --accent
    "pista": hexa("#4a3f36"),        # --border (segmentos inactivos)
}

_W = "C:/Windows/Fonts/"
_L = "/usr/share/fonts/"
_M = "/System/Library/Fonts/"
FUENTES = {
    "titulo": [_W + "segoeuib.ttf", _L + "opentype/inter/InterDisplay-Bold.otf",
               _L + "truetype/dejavu/DejaVuSans-Bold.ttf", _M + "Helvetica.ttc"],
    "texto": [_W + "segoeui.ttf", _L + "opentype/inter/Inter-Regular.otf",
              _L + "truetype/dejavu/DejaVuSans.ttf", _M + "Helvetica.ttc"],
    "mono": [_W + "consola.ttf", _L + "truetype/dejavu/DejaVuSansMono.ttf", _M + "Menlo.ttc"],
    "mono_bold": [_W + "consolab.ttf", _L + "truetype/dejavu/DejaVuSansMono-Bold.ttf",
                  _M + "Menlo.ttc"],
}

MARCA = "Claude Code desde cero · curso gratuito en español"

# Frase corta para redes: el objetivo completo es demasiado largo para leerse en un celular.
GANCHOS = {
    1: "Instala, entiende el ciclo agéntico y crea tu primer proyecto",
    2: "Diffs visuales, @-menciones y checkpoints en tu editor",
    3: "Prompts que Claude puede verificar por sí solo",
    4: "CLAUDE.md, reglas por ruta y memoria automática",
    5: "Decide cuánta autonomía darle a Claude y protege tu código",
    6: "Conecta la documentación, GitHub y tu base de datos",
    7: "Reglas que se cumplen siempre, también en Windows",
    8: "Delega con contexto limpio y trabaja en paralelo",
    9: "Empaqueta tu flujo de trabajo y compártelo",
    10: "Reportes por comuna con todo lo aprendido",
}


def fuente(clave, tam):
    import os
    extra = os.environ.get("OG_FUENTES_DIR")
    rutas = ([str(Path(extra) / Path(r).name) for r in FUENTES[clave]] if extra else []) + FUENTES[clave]
    for ruta in rutas:
        if Path(ruta).exists():
            return ImageFont.truetype(ruta, tam)
    sys.exit(f"No encontré fuente para '{clave}'. Revisa FUENTES u OG_FUENTES_DIR.")


def envolver(draw, texto, fnt, ancho_max):
    lineas, actual = [], ""
    for palabra in texto.split(" "):
        prueba = f"{actual} {palabra}".strip()
        if draw.textlength(prueba, font=fnt) <= ancho_max:
            actual = prueba
        else:
            lineas.append(actual)
            actual = palabra
    lineas.append(actual)
    return lineas


def titulo_ajustado(draw, texto, ancho_max, max_lineas=2):
    """Reduce el tamaño hasta que el título quepa en max_lineas."""
    for tam in range(76, 40, -2):
        fnt = fuente("titulo", tam)
        lineas = envolver(draw, texto, fnt, ancho_max)
        if len(lineas) <= max_lineas:
            return fnt, lineas, tam
    return fnt, lineas[:max_lineas], tam


def lienzo():
    img = Image.new("RGB", (ANCHO, ALTO), COLORES["fondo"])
    d = ImageDraw.Draw(img)
    # Marco interior sutil, como una ventana de terminal
    d.rounded_rectangle((24, 24, ANCHO - 24, ALTO - 24), radius=20,
                        outline=COLORES["fondo_borde"], width=2)
    # Tres puntos de ventana
    for i, c in enumerate([COLORES["acento"], COLORES["suave"], COLORES["pista"]]):
        d.ellipse((52 + i * 22, 46, 64 + i * 22, 58), fill=c)
    return img, d


def barra_progreso(d, actual, y):
    segmentos, sep = 10, 8
    ancho_total = 420
    ancho_seg = (ancho_total - sep * (segmentos - 1)) / segmentos
    for i in range(segmentos):
        x = MARGEN + i * (ancho_seg + sep)
        color = COLORES["acento"] if i + 1 <= actual else COLORES["pista"]
        d.rounded_rectangle((x, y, x + ancho_seg, y + 10), radius=5, fill=color)


def pie(d):
    fnt = fuente("texto", 24)
    d.text((MARGEN, ALTO - 78), MARCA, font=fnt, fill=COLORES["suave"])


def imagen_modulo(numero, titulo, semana):
    img, d = lienzo()
    num = f"{numero:02d}"

    # Número gigante decorativo a la derecha
    fnt_num = fuente("mono_bold", 240)
    w = d.textlength(num, font=fnt_num)
    d.text((ANCHO - w - 56, 140), num, font=fnt_num, fill=COLORES["fondo_borde"])

    # Prompt de terminal
    fnt_prompt = fuente("mono", 26)
    prompt = f"$ claude --modulo {numero}"
    d.text((MARGEN, 104), prompt, font=fnt_prompt, fill=COLORES["suave"])
    cx = MARGEN + d.textlength(prompt + " ", font=fnt_prompt)
    d.rectangle((cx, 108, cx + 14, 134), fill=COLORES["acento"])

    # Etiqueta
    etiqueta = "PROYECTO FINAL · SEMANA 10" if numero == 10 else f"MÓDULO {num} · SEMANA {semana}"
    d.text((MARGEN, 176), etiqueta, font=fuente("mono_bold", 26), fill=COLORES["acento"])

    # Título
    ancho_texto = 760  # no invade el número decorativo
    # Espacio no separable para que los nombres de producto no se partan
    for nombre in ("Claude Code", "VS Code"):
        titulo = titulo.replace(nombre, nombre.replace(" ", "\u00a0"))
    fnt_t, lineas, tam = titulo_ajustado(d, titulo, ancho_texto)
    y = 224
    for linea in lineas:
        d.text((MARGEN, y), linea, font=fnt_t, fill=COLORES["texto"])
        y += int(tam * 1.12)

    # Gancho: siempre en una línea; si no cabe, se reduce la letra (mínimo 26 px)
    gancho = GANCHOS.get(numero, "")
    ancho_gancho = ANCHO - MARGEN * 2 - 40
    tam_g = 32
    while tam_g > 26 and d.textlength(gancho, font=fuente("texto", tam_g)) > ancho_gancho:
        tam_g -= 1
    d.text((MARGEN, y + 18), gancho, font=fuente("texto", tam_g), fill=COLORES["suave"])

    barra_progreso(d, numero, ALTO - 128)
    pie(d)
    return img


def imagen_landing():
    img, d = lienzo()
    fnt_prompt = fuente("mono", 26)
    prompt = "$ claude"
    d.text((MARGEN, 104), prompt, font=fnt_prompt, fill=COLORES["suave"])
    cx = MARGEN + d.textlength(prompt + " ", font=fnt_prompt)
    d.rectangle((cx, 108, cx + 14, 134), fill=COLORES["acento"])

    d.text((MARGEN, 176), "CURSO GRATUITO · 10 SEMANAS", font=fuente("mono_bold", 26),
           fill=COLORES["acento"])
    fnt_t = fuente("titulo", 80)
    y = 222
    for linea in ["Domina Claude Code", "con 40 minutos al día"]:
        d.text((MARGEN, y), linea, font=fnt_t, fill=COLORES["texto"])
        y += 92
    d.text((MARGEN, y + 22), "Programa con IA sin dejar de pensar como desarrollador.",
           font=fuente("texto", 32), fill=COLORES["suave"])
    barra_progreso(d, 10, ALTO - 128)
    pie(d)
    return img


def guardar(img, ruta):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    img.save(ruta, "PNG", optimize=True)
    kb = ruta.stat().st_size / 1024
    aviso = "  <-- supera 300 KB" if kb > 300 else ""
    print(f"{ruta.relative_to(RAIZ)}  {kb:.0f} KB{aviso}")


def main():
    archivos = sorted(MODULOS.glob("*.md"))
    if not archivos:
        sys.exit(f"No encontré módulos en {MODULOS}")
    for archivo in archivos:
        fm = yaml.safe_load(archivo.read_text(encoding="utf-8").split("---")[1])
        if "numero" not in fm or fm["numero"] < 1:
            continue  # 00-como-usar u otros sin número de módulo
        img = imagen_modulo(fm["numero"], fm["titulo"], fm.get("semana", fm["numero"]))
        guardar(img, SALIDA / f"{archivo.stem}.png")
    guardar(imagen_landing(), SALIDA / "og-default.png")


if __name__ == "__main__":
    main()
