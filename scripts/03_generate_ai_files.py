#!/usr/bin/env python3
"""
Genera README.md, llms.txt y AGENTS.md orientados a IAs.
"""

from pathlib import Path
from datetime import datetime

ROOT = Path(".")

README = f"""# Investment Library

Biblioteca personal de conocimiento sobre inversión, estrategia y modelos mentales.

> **Nota**: Este repositorio contiene material de estudio personal.  
> No es consejo de inversión. Verifica siempre las fuentes originales y respeta los derechos de autor.

## Estructura
books/
├── value-investing/     # Graham, Buffett, Fisher, Lynch...
├── mental-models/       # Munger, sesgos, thinking
├── strategy-moats/      # 7 Powers, competitive advantage
├── macro-cycles/        # Dalio, capital cycles
├── valuation/           # Damodaran y valoración
├── quantitative/        # Finanzas cuantitativas
├── psychology-money/    # Housel y psicología del dinero
└── other/

## Cómo usar con IAs

- **Claude**: conecta el repo vía GitHub integration.
- **Cursor / Windsurf**: abre la carpeta y usa `@books`.
- **RAG propio**: indexa la carpeta `books/` con LangChain, LlamaIndex, AnythingLLM, etc.
- Lee también `llms.txt` y `AGENTS.md` para instrucciones específicas.

## Actualizado

{datetime.now().strftime("%Y-%m-%d")}
"""

LLMS_TXT = """# llms.txt – Instrucciones para modelos de lenguaje

Este repositorio es una biblioteca de conocimiento de inversión.

## Propósito
Servir como base de conocimiento (RAG / context) para preguntas sobre:
- Value investing y análisis fundamental
- Modelos mentales y sesgos cognitivos
- Estrategia competitiva y moats
- Ciclos macro y capital cycle
- Valoración de empresas
- Psicología del dinero

## Cómo usar el contenido
1. Prioriza los archivos dentro de `books/`.
2. Cuando cites ideas, indica el libro/autor de origen si es posible.
3. No inventes citas textuales largas. Resume y atribuye.
4. Si el usuario pide consejo de inversión concreto, aclara que no es consejo profesional.

## Estructura recomendada de respuesta
- Resume la idea clave del material relevante.
- Da el contexto del autor/libro.
- Añade matices o limitaciones cuando sea apropiado.
"""

AGENTS_MD = """# AGENTS.md

## Contexto del proyecto
Repositorio de conocimiento de inversión organizado para uso con agentes de IA.

## Reglas para el agente
- Trabaja principalmente con los archivos de la carpeta `books/`.
- Cuando respondas, basa tus afirmaciones en el contenido disponible.
- Si no encuentras información suficiente en el repo, dilo claramente.
- Nunca presentes el contenido como consejo de inversión personalizado.
- Prefiere resúmenes claros + atribución al autor/libro.

## Comandos útiles (ejemplo)
- Buscar por tema: listar archivos en `books/value-investing/`, etc.
- Resumir un libro concreto.
- Comparar ideas entre dos autores (ej. Graham vs Fisher).
"""

def main():
    (ROOT / "README.md").write_text(README, encoding="utf-8")
    (ROOT / "llms.txt").write_text(LLMS_TXT, encoding="utf-8")
    (ROOT / "AGENTS.md").write_text(AGENTS_MD, encoding="utf-8")
    print("✓ Generados: README.md, llms.txt, AGENTS.md")

if __name__ == "__main__":
    main()
