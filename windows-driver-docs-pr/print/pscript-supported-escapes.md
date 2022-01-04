---
title: Pscript-Supported Escapes
description: Pscript-Supported Escapes
keywords:
- PostScript Printer Driver WDK print , escapes
- Pscript WDK print , escapes
- escapes WDK Pscript
ms.date: 03/28/2021
---

# Pscript-Supported Escapes

The Pscript5 printer driver supports the following escapes.

| Escape | Description |
|--|--|
| BEGIN_PATH | Open a path. |
| CHECKJPEGFORMAT | Determine whether a printer can handle a JPEG image. For more information about this escape, see [CHECKJPEGFORMAT](/previous-versions/windows/desktop/legacy/dd183421(v=vs.85)).<br><br>This escape produces a call to the [DrvQueryDeviceSupport](/windows/win32/api/winddi/nf-winddi-drvquerydevicesupport) function. |
| CHECKPNGFORMAT | Determine whether a printer can handle a PNG image. For more information about this escape, see [CHECKPNGFORMAT](/previous-versions/windows/desktop/legacy/dd183424(v=vs.85)).<br><br>This escape produces a call to the [DrvQueryDeviceSupport](/windows/win32/api/winddi/nf-winddi-drvquerydevicesupport) function. |
| CLIP_TO_PATH | Define a clip region that is bounded by a path. |
| DOWNLOADHEADER | Download all of the procsets (that is, sets of PostScript procedures). |
| DRAWPATTERNRECT | Create a white, grayscale, or solid black rectangle by using the pattern and rule capabilities of Page Control Language (PCL) on Hewlett Packard LaserJet or LaserJet-compatible printers. A grayscale is a gray pattern that contains a specific mixture of black and white pixels. For more information about this escape, see [DRAWPATTERNRECT](/previous-versions/windows/desktop/legacy/dd162495(v=vs.85)).<br><br>This escape is associated with the driver's [DrvEscape](/windows/win32/api/winddi/nf-winddi-drvescape) function. |
| ENCAPSULATED_POSTSCRIPT | Send Encapsulated PostScript (EPS) data to the printer.<br><br>This escape is associated with the driver's [DrvDrawEscape](/windows/win32/api/winddi/nf-winddi-drvdrawescape) function. |
| END_PATH | End a path. |
| EPSPRINTING | Indicate the start or end of EPS printing.<br><br>The graphics device interface (GDI) intercepts this escape and translates it to a DDI call other than DrvEscape. The printer driver does not receive this escape. |
| GET_PS_FEATURESETTING | Get information about a specified feature setting for a PostScript driver.<br><br>For more information about this escape, see [GET_PS_FEATURESETTING](/previous-versions/windows/desktop/legacy/dd144954(v=vs.85)). |
| GETTECHNOLOGY | Get the general technology type for a printer. Printer drivers that are written for versions of the Windows operating system after Windows 3.0 might not support this escape. |
| PASSTHROUGH | Send data directly to a PostScript printer driver in compatibility mode or GDI-centric mode. PostScript printer drivers in PostScript-centric mode do not support this escape.<br><br>For more information about this escape, see [PASSTHROUGH](/previous-versions/windows/desktop/legacy/dd162776(v=vs.85)). |
| POSTSCRIPT_DATA | Send data directly to a printer driver. This escape is identical to the PASSTHROUGH escape except that PostScript printer drivers support this escape in Windows NT 4.0 compatibility mode only.<br><br>For more information about this escape, see [POSTSCRIPT_DATA](/previous-versions/windows/desktop/legacy/dd162828(v=vs.85)). |
| POSTSCRIPT_IDENTIFY | Set a PostScript printer driver to GDI-centric or PostScript-centric mode.<br><br>For more information about this escape, see [POSTSCRIPT_IDENTIFY](/previous-versions/windows/desktop/legacy/dd162829(v=vs.85)). |
| POSTSCRIPT_IGNORE | Suppress output.<br><br> |
| POSTSCRIPT_INJECTION | Insert a block of raw data in a PostScript job stream.<br><br> |
| POSTSCRIPT_PASSTHROUGH | Send data directly to a PostScript printer driver in Windows NT 4.0 compatibility mode or PostScript-centric mode. PostScript printer drivers in GDI-centric mode do not support this escape.<br><br> |
| QUERYESCSUPPORT | Determine whether the device driver implements a particular escape.<br><br> |
| SETCOPYCOUNT | Set the number of copies to be printed.<br><br>This escape has been superseded by the [DocumentProperties](/windows/win32/printdocs/documentproperties) and [PrinterProperties](/windows/win32/printdocs/printerproperties) functions. |
| SPCLPASSTHROUGH2 | Enable applications to include private procedures and other resources at the document level-save context.<br><br>For more information about this escape, see [SPCLPASSTHROUGH2](/previous-versions/windows/desktop/legacy/dd145110(v=vs.85)). |
