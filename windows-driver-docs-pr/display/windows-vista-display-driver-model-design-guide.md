---
title: Windows Display Driver Model (WDDM) Design Guide
description: The Windows Display Driver Model (WDDM) is available starting with Windows Vista and is required starting with Windows 8. This section discusses requirements, specifications, and behavior for WDDM drivers.
ms.assetid: d9dc0d48-aea4-4614-a23b-e2449800469f
keywords: ["WDDM Design Guide WDK", "display driver model WDK Windows Vista", "Windows Vista display driver model WDK", "display devices WDK", "display drivers WDK , Windows Vista", "display driver model WDK Windows Vista , about display driver model", "Windows Vista display driver model WDK , about display driver model", "miniport drivers WDK display", "display miniport drivers WDK See miniport drivers WDK display"]
---

# Windows Display Driver Model (WDDM) Design Guide


The Windows Display Driver Model (WDDM) is available starting with Windows Vista and is required starting with Windows 8. This section discusses requirements, specifications, and behavior for WDDM drivers.

## <span id="wddm_id"></span><span id="WDDM_ID"></span>


**Note**  [Windows 2000 Display Driver Model (XDDM)](windows-2000-display-driver-model-design-guide.md) and VGA drivers will not compile on Windows 8 and later versions. If display hardware is attached to a Windows 8 computer without a driver that is certified to support WDDM 1.2 or later, the system defaults to running the Microsoft Basic Display Driver.

 

The following sections describe the Windows Display Driver Model (WDDM):

[What's new for Windows 10 display drivers (WDDM 2.0)](what-s-new-for-windows-threshold-display-drivers--wddm-2-0-.md)

[What's new for Windows 8.1 display drivers (WDDM 1.3)](what-s-new-for-windows-8-1-display-drivers--wddm-1-3-.md)

[What's new for Windows 8 display drivers (WDDM 1.2)](what-s-new-for-windows-8-display-drivers.md)

[What's new for Windows 7 display drivers (WDDM 1.1)](what-s-new-for-windows-7-display-drivers--wddm-1-1-.md)

[WDDM 2.0 and Windows 10](wddm-2-0-and-windows-10.md)

[WDDM 1.2 and Windows 8](wddm-in-windows-8.md)

[Introduction to the Windows Display Driver Model (WDDM)](introduction-to-the-windows-vista-and-later-display-driver-model.md)

[Installation Requirements for Display Miniport and User-Mode Display Drivers](installing-display-miniport-and-user-mode-display-drivers.md)

[Installation Requirements for Display Drivers Optimized for Windows 7 and Later](installing-display-drivers-optimized-for-windows-7-and-later.md)

[Initializing Display Miniport and User-Mode Display Drivers](initializing-display-miniport-and-user-mode-display-drivers.md)

[Windows Vista Display Driver Threading and Synchronization Model](windows-vista-display-driver-threading-and-synchronization-model.md)

[Video Memory Management and GPU Scheduling](video-memory-management-and-gpu-scheduling.md)

[User-Mode Display Drivers](user-mode-display-drivers.md)

[Monitor Drivers](monitor-drivers.md)

[Multiple Monitors and Video Present Networks](multiple-monitors-and-video-present-networks.md)

[Tasks in the Windows Display Driver Model (WDDM)](tasks-in-the-windows-vista-display-driver-model.md)

[Debugging Tips for the Windows Display Driver Model (WDDM)](debugging-tips-for-the-windows-vista-display-driver-model.md)

[Implementation Tips and Requirements for the Windows Display Driver Model (WDDM)](implementation-tips-and-requirements-for-the-windows-vista-display-dri.md)

[Display Samples](display-samples.md)

**Note**  WDDM drivers do not directly use services of the Windows Graphics Device Interface (GDI) engine; therefore, the [GDI](gdi.md) section is not relevant to writing display drivers for the WDDM driver model.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Windows%20Display%20Driver%20Model%20%28WDDM%29%20Design%20Guide%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




