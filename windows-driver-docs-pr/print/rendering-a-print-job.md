---
title: Rendering a Print Job
description: Rendering a Print Job
keywords:
- printer graphics DLL WDK , rendering print jobs
- graphics DLL WDK printer , rendering print jobs
- rendering print jobs WDK
- jobs WDK print , rendering
- print jobs WDK , rendering
- banding WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Rendering a Print Job





Print jobs are either rendered as they are created, or they are written to a spool file as EMF records. In the case of EMF records, rendering takes place when the EMF *print processor* (localspl.dll) plays back the records. Rendering consists of a series of calls to the user-mode GDI drawing functions, beginning with **CreateDC** (described in the Microsoft Windows SDK documentation). The call to **CreateDC** is the first in a series of application calls that lead to a chain of actions involving the graphics rendering engine (GRE, also known as kernel-mode GDI), and the printer graphics DLL.

The following figure shows the interaction between kernel-mode GDI and the printer graphics DLL after **CreateDC** is called.

![diagram illustrating the interaction between kernel-mode gdi and the printer graphics dll after createdc is called.](images/gdirendr2.png)

1.  When an application calls the **CreateDC** function to create a printer device context, GDI checks to see if the appropriate printer graphics DLL is loaded. If it is not, GDI loads the DLL and calls the [**DrvEnableDriver**](/windows/win32/api/winddi/nf-winddi-drvenabledriver) function in the DLL. The function is not called again unless the driver is reloaded.

2.  Next, GDI calls the printer graphics DLL's [**DrvEnablePDEV**](/windows/win32/api/winddi/nf-winddi-drvenablepdev) function so the driver can create a physical device instance and return device characteristics. GDI uses the returned information to create an internal description of the device instance.

3.  GDI then calls the graphics DLL's [**DrvCompletePDEV**](/windows/win32/api/winddi/nf-winddi-drvcompletepdev) function to supply a GDI handle to the device instance. The graphics DLL must use this handle as input to some of the **Eng**-prefixed callbacks provided by the GDI drawing engine (see [GDI Support Services](../display/gdi-support-services.md)).

4.  After GDI receives the device instance handle, it then makes a call to the graphics DLL's [**DrvEnableSurface**](/windows/win32/api/winddi/nf-winddi-drvenablesurface) function, which sets up the surface for drawing, and associates it with the physical device instance.

5.  The driver can create a drawing surface for the device instance by calling [**EngCreateBitmap**](/windows/win32/api/winddi/nf-winddi-engcreatebitmap). Alternatively, if the drawing surface is device-managed, the driver can call [**EngCreateDeviceSurface**](/windows/win32/api/winddi/nf-winddi-engcreatedevicesurface).

6.  If **EngCreateBitmap** cannot supply a bitmap large enough to contain an entire physical page, and if the driver supports page banding, [**EngMarkBandingSurface**](/windows/win32/api/winddi/nf-winddi-engmarkbandingsurface) can be called to inform GDI that banding will be employed.

7.  Finally, the [**EngAssociateSurface**](/windows/win32/api/winddi/nf-winddi-engassociatesurface) must be called to allow GDI to associate the created surface with a specified device instance, and to let GDI know which driver-supplied graphics DDI drawing functions (if any) it should call when it draws on this particular surface.

At this point, a drawing surface has been created and rendering can begin. The functions that GDI calls depend on whether banding is in effect.

### Banding in use

For each document to be rendered when banding is used, GDI calls the following functions in the printer graphics DLL:

[**DrvStartDoc**](/windows/win32/api/winddi/nf-winddi-drvstartdoc)
For each physical page {
[**DrvStartPage**](/windows/win32/api/winddi/nf-winddi-drvstartpage)
[**DrvStartBanding**](/windows/win32/api/winddi/nf-winddi-drvstartbanding)
For each banding pass on a physical page{
[*DrvQueryPerBandInfo*](/windows/win32/api/winddi/nf-winddi-drvqueryperbandinfo)
Rendering operations
[**DrvNextBand**](/windows/win32/api/winddi/nf-winddi-drvnextband) // Send raster data for this band, then clear surface to reuse with next band
    }
}
[**DrvEndDoc**](/windows/win32/api/winddi/nf-winddi-drvenddoc)
### <a href="" id="banding-not-in-use"></a> Banding not in use

For each document to be rendered when banding is not used, GDI calls the following functions in the printer graphics DLL:

[**DrvStartDoc**](/windows/win32/api/winddi/nf-winddi-drvstartdoc)
For each physical page
[**DrvStartPage**](/windows/win32/api/winddi/nf-winddi-drvstartpage)
Rendering operations
[*DrvSendPage*](/windows/win32/api/winddi/nf-winddi-drvsendpage) // Send raster data for the page
}
[**DrvEndDoc**](/windows/win32/api/winddi/nf-winddi-drvenddoc)
With the exception of [*DrvQueryPerBandInfo*](/windows/win32/api/winddi/nf-winddi-drvqueryperbandinfo), these functions are intended to allow the printer graphics DLL to send control sequences to the printer hardware (by calling [**EngWritePrinter**](/windows/win32/api/winddi/nf-winddi-engwriteprinter)), and to perform any internal operations needed to initialize or complete processing of a document, page, or band.

The printer graphics DLL is responsible for sending the rendered image (that is, the contents of the drawing surface) to the printer at appropriate times (by calling **EngWritePrinter**), as follows:

-   For GDI-managed or device-managed bitmap surfaces

    The drawing surface is a GDI-supplied or driver-supplied bitmap. The printer graphics DLL might hook some drawing functions (see [Surface Negotiation](../display/surface-negotiation.md)). If page banding is in use, the [**DrvNextBand**](/windows/win32/api/winddi/nf-winddi-drvnextband) function should send drawing surface contents. If banding is not in use, the [*DrvSendPage*](/windows/win32/api/winddi/nf-winddi-drvsendpage) function should send the drawing surface contents.

-   For device-managed vector surfaces

    The drawing surface is within the device. The printer graphics DLL hooks all drawing functions (see [Surface Negotiation](../display/surface-negotiation.md)), and these functions send image data to the printer during rendering operations. Page banding is not used.

If you anticipate that any graphics DDI function provided by a printer graphics DLL could potentially take more than five seconds to execute, you should include code that calls [**EngCheckAbort**](/windows/win32/api/winddi/nf-winddi-engcheckabort) at least every five seconds to see if the print job should be terminated.

After GDI calls [**DrvEndDoc**](/windows/win32/api/winddi/nf-winddi-drvenddoc) to indicate that a document has been completely rendered, it calls [**DrvDisableSurface**](/windows/win32/api/winddi/nf-winddi-drvdisablesurface). If [**DrvEnableSurface**](/windows/win32/api/winddi/nf-winddi-drvenablesurface) called [**EngCreateBitmap**](/windows/win32/api/winddi/nf-winddi-engcreatebitmap), then **DrvDisableSurface** must call [**EngDeleteSurface**](/windows/win32/api/winddi/nf-winddi-engdeletesurface).

GDI calls a printer graphics DLL's [**DrvDisablePDEV**](/windows/win32/api/winddi/nf-winddi-drvdisablepdev) function when an application calls **DeleteDC**.

If an application calls **ResetDC** function during the printing of a document, GDI creates a new device context and calls the printer graphics DLL's [**DrvEnablePDEV**](/windows/win32/api/winddi/nf-winddi-drvenablepdev) function for the new context. Then GDI calls the [**DrvResetPDEV**](/windows/win32/api/winddi/nf-winddi-drvresetpdev) function, so the graphics DLL can update the new context with information from the old one. Next, [**DrvDisableSurface**](/windows/win32/api/winddi/nf-winddi-drvdisablesurface) and [**DrvDisablePDEV**](/windows/win32/api/winddi/nf-winddi-drvdisablepdev) are called for the old context, followed by [**DrvEnableSurface**](/windows/win32/api/winddi/nf-winddi-drvenablesurface) for the new context. Finally, GDI calls [**DrvStartDoc**](/windows/win32/api/winddi/nf-winddi-drvstartdoc) and rendering resumes on a new page.

GDI calls [**DrvDisableDriver**](/windows/win32/api/winddi/nf-winddi-drvdisabledriver) prior to unloading the printer graphics DLL.

If printer hardware supports drawing operations that are not supported by GDI drawing functions, the printer graphics DLL can provide a [**DrvDrawEscape**](/windows/win32/api/winddi/nf-winddi-drvdrawescape) function.

A printer graphics DLL can provide a [**DrvEscape**](/windows/win32/api/winddi/nf-winddi-drvescape) function if it is necessary to support drawing or nondrawing operations that are not available through GDI functions. For example, the [Microsoft PostScript printer driver](microsoft-postscript-printer-driver.md) uses escapes to support PostScript injection points. Or, an application might need to obtain a fax machine's phone number. The **DrvEscape** function is also used for indicating the operations supported by the **DrvDrawEscape** function.

**CreateDC**, **ResetDC**, and **DeleteDC** are described in the Microsoft Windows SDK documentation.

 

