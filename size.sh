#!/bin/bash
#анализ размера файлов и директорий.
du -sh * 2>/dev/null | sort -hr
