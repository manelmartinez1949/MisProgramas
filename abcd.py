Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\manel\AppData\Local\Programs\Python\Python312\Leer Texto de Foto.py
Traceback (most recent call last):
  File "C:\Users\manel\AppData\Local\Programs\Python\Python312\Lib\site-packages\pytesseract\pytesseract.py", line 275, in run_tesseract
    proc = subprocess.Popen(cmd_args, **subprocess_args())
  File "C:\Users\manel\AppData\Local\Programs\Python\Python312\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "C:\Users\manel\AppData\Local\Programs\Python\Python312\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
FileNotFoundError: [WinError 2] El sistema no puede encontrar el archivo especificado

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\manel\AppData\Local\Programs\Python\Python312\Leer Texto de Foto.py", line 8, in <module>
    text = pytesseract.image_to_string(img)
  File "C:\Users\manel\AppData\Local\Programs\Python\Python312\Lib\site-packages\pytesseract\pytesseract.py", line 486, in image_to_string
    return {
  File "C:\Users\manel\AppData\Local\Programs\Python\Python312\Lib\site-packages\pytesseract\pytesseract.py", line 489, in <lambda>
    Output.STRING: lambda: run_and_get_output(*args),
  File "C:\Users\manel\AppData\Local\Programs\Python\Python312\Lib\site-packages\pytesseract\pytesseract.py", line 352, in run_and_get_output
    run_tesseract(**kwargs)
  File "C:\Users\manel\AppData\Local\Programs\Python\Python312\Lib\site-packages\pytesseract\pytesseract.py", line 280, in run_tesseract
    raise TesseractNotFoundError()
pytesseract.pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
