# pdfviewer

A simple PDF viewer based on [mozilla](https://github.com/mozilla)/[pdf.js](https://github.com/mozilla/pdf.js). The gadget powered by Python flask and bundled its applications and dependencies into a single executable package for Windows.

The pdfviewer is in order to work with the [talentranslate](https://microsoftedge.microsoft.com/addons/detail/talent%E5%88%92%E8%AF%8D%E7%BF%BB%E8%AF%91/emelgiiiemoiljnmikcgbmjkapalgcme)(a browser extension) for local PDF files translation.

## How to build

### Environments

I recommend that you create a virtual environments:

```
D:\pdfviewer> python -m venv venv
```

Enter the virtual environments:

```
D:\pdfviewer> venv\Scripts\activate
```

These commands above is run in the Microsoft Windows command prompt windows(cmd.exe).

### Python requirements

```
(venv) D:\pdfviewer> pip install flask pyinstaller
```

If you have a terrible download speed, you can use the option `-i <mirror for pip>`, for instance, in China:

```
(venv) D:\pdfviewer> pip install flask pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### Build

You have two choices, one is onefile version and one is onedir version.

Onefile version:

```
(venv) D:\pdfviewer> pyinstaller pdfviewer_onefile.spec
```

Onedir version:

```
(venv) D:\pdfviewer> pyinstaller pdfviewer_onedir.spec
```
