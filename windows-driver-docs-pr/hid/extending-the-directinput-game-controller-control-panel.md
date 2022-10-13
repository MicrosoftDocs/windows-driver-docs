---
title: Extending the DirectInput game controller control panel
description: Extending the DirectInput game controller control panel
keywords:
- property sheets WDK DirectInput
- game controllers WDK DirectInput
- control panels WDK DirectInput
- joysticks WDK HID , game controller support
- force feedback drivers WDK HID , property sheets
- game pad support WDK DirectInput
ms.date: 10/11/2022
---

# Extending the DirectInput game controller control panel

This topic describes creating property sheets for the Microsoft DirectInput game controller control panel.

## About the DirectInput control panel

DirectInput provides support for game controllers such as game pads, joysticks, and force-feedback devices. In Microsoft DirectX 5.0 and later versions, DirectInput provides a new game controller control panel called *joy.cpl*. Control Panel allows extensibility in that the property sheets that are displayed for each controller can be replaced with property pages that are specific to that controller. This is done through the creation of a DLL that contains information about these property sheets. This DLL exposes a COM interface that is called into by the DirectInput control panel.

Game controller hardware vendors are encouraged to use this extensibility feature to provide customized property sheets for their game controllers instead of creating a separate control panel. This allows the user to open a single control panel to configure and test their game controllers.

## DirectInput control panel architecture

This section describes the basic structure of the DirectInput control panel extensible property sheets.

### Game controller control panel

The basic architecture of the DirectInput control panel consists of the DirectInput game controller control panel, the abstraction-layer library that supports the **IDIGameCntrlPropSheet** COM interface, and a COM object for each game controller property sheet.

> [!NOTE]
> The word "object" describes an entity created by CreateInstance to support the methods of a COM interface, even when these methods are not being called through an object-oriented programming language such as C++. The word "sheet" describes the dialog into which the pages insert. The word "page" describes the content dialogs of the "property sheet" dialog.

The DirectInput control panel works directly with DirectInput, which in turn works directly with device drivers. As a by-product of this, the DirectInput control panel has access to input devices even when the application is in the background.

### The default analog device property sheet

Hardware vendors who do not create their own control panel use the services of the default analog device property sheet supplied by Gcdef.dll. Any controller that does not have a **ConfigCLSID** key in the registry under its **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\MediaProperties\\PrivateProperties\\Joystick\\OEM\\**\<CONTROLLER\_NAME\> entry uses this default property sheet. This property sheet contains the following two pages:

- **Test:** This page demonstrates that the device is responding properly. It returns a graphical representation of the registry settings that are associated with the device attributes and allows the user to view them.

- **Settings:** This page allows the user to write specific information about the device to the system. Services are provided for calibration and for a rudder or pedals.

### Integration with Windows

Because the property sheet page is a COM object, it must be registered with Windows. This can be done by an INF file or through DirectInput's **IDirectInputJoyConfig8** interface. A sample INF file is part of the sample property sheet in the DirectX Driver Development Kit (DDK).

**To register the property sheet page:**

1. Use the GuidGen tool (which is included in the Microsoft Windows SDK) to create a CLSID for your property sheet (this is the same as the one entered in the **ConfigCLSID** entry mentioned earlier). Remember, this is your device-specific property sheet GUID and it should be the same as the one in your code.

1. Create a new key in the registry under **My Computer\\HKEY\_CLASSES\_ROOT\\CLSID** using this new GUID. It should look something like {B9EA2BE1-E8E9-11D0-9880-00AA0044480F}.

1. Inside that key, create subkeys named **InProcHandler32** and **InProcServer32**.

1. Inside the **InProcServer32** key, edit the default entry to reflect the location and name of your property sheet DLL.

Your device must also be properly registered as a gaming device. This may be done through DirectInput, or through an INF file.

**To register the device:**

1. In the registry key **My Computer\\HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\control\\MediaProperties\\PrivateProperties\\Joystick\\OEM**, enter a key for your device. Make this key name the same as your device OEM Name.

1. Create the following entries:

   | Key Value | Key value type | Key value type contents |
   |--|--|--|
   | ConfigCLSID | String Value | "{your property sheet CLSID}" |
   | OEMName | String Value | "Product name of your device" |

   > [!NOTE]
   > These two entries are the minimum you need to get started. Refer to the Windows SDK for additional information about all of the available entries and their associated services.

## DirectInput control panel essentials

This section introduces the concepts and components of the DirectInput control panel, and provides information to help you begin implementing your own device-specific property sheet.

### Files and your build environment

You will need the Windows Software Development Kit (SDK). The *dinputd.h* header file provides the necessary interface, structures, class definitions, and errors. Use DirectInput's **IDirectInputJoyConfig8** interface for all registry access. If you plan to use DirectInput in your property page, you must also used the associated Windows SDK files. All structures in the DirectInput control panel are packed on 8-byte boundaries. Verify that your property sheet packs structures on 8-byte boundaries.

> [!NOTE]
> When testing your control panel, make sure to test it on a system whose primary display is set to a resolution of 640 x 480 pixels. Make sure that all the controls are still visible at this reduced resolution.

## Creating your property sheet

This example demonstrates many aspects of DirectInput and provides a good starting point for your own custom property sheet.

### Create your own property sheet

Creating a custom property sheet from scratch is a relatively simple process.

1. Create a GUID to identify your property page:

   - Using the GuidGen tool (which is included in the Windows SDK), create a GUID for your property page (only one, no matter how many pages). Define this in your application-specific include file.
   - Create the required DllGetClassObject and DllCanUnloadNow.
   - Create an implementation for the COM ClassFactory defined in *dinputd.h*.
   - Create the implementation for the **IDIGameCntrlPropSheet** interface.
   - Using RegEdit, add your defined GUID to the **My Computer\\HKEY\_CLASSES\_ROOT\\CLSID** key. Then add the keys InProcHandler32 and InProcServer32 to your key.
   - Modify the (default) entry of the InProcServer32 entry to point to the location of your property sheet DLL. An example would be: "C:\\my\_device\\my\_propertysheet.dll". This example shows a ProgID entry. This is not necessary, but is often used to store information about the module residing at that GUID.

1. Create dialog templates and dialog procedures as you would for any Windows application.

   > [!NOTE]
   > You may want to write a test container for your property sheets as a window that launches your pages as independent dialog boxes. At this point, you could also convert any existing control panel you might have to the DirectInput control panel.

1. Populate the **[DIGCPAGEINFO](/previous-versions/windows/hardware/drivers/ff538484(v=vs.85))** and **[DIGCSHEETINFO](/previous-versions/windows/hardware/drivers/ff538492(v=vs.85))** structures and return that information in your implementations of **[IDIGameCntrlPropSheet::GetPageInfo](/previous-versions/windows/hardware/drivers/ff540026(v=vs.85))** and **[IDIGameCntrlPropSheet::GetSheetInfo](/previous-versions/windows/hardware/drivers/ff540029(v=vs.85))** respectively.

The generation of the property sheet pages is done through the **PropertySheet** function. All behaviors of this function are inherent in the property sheet pages. For example, the property sheet page reflects the largest dialog template that it receives. If the user creates one page and its associated template is very small, this reflects directly on the size of the resulting dialog.

Dialog templates are also important to remember when considering visual alignment and the centering of controls on a page. For example, consider a case in which the user creates two pages that contain items specified to be centered on the page. One item to be centered is 200 dialog units (DLUs) in width; the other is 100 units. In such a case, the latter item is not centered on the page. Instead, the control is centered to its template and additional white space (or gray, as it may be) is added to the width of the more narrow page. You should create dialog templates of the same size, even if you are not using it all. (For more information about the **PropertySheet** function, see the Windows SDK.)

### Testing your property sheet

Run the debug version of both DirectInput and the DirectInput control panel during the testing of your property sheet page. DirectX components are designed to issue useful errors and warning messages to the debug window/terminal.

Debugging a control panel application can be tricky. Use the following steps to debug a custom property sheet page in Microsoft Developer Studio 5.0 and newer (other compilers have similar behavior).

1. From the **Project** menu, select **Settings**.

1. Select the **Debug** tab.

1. For the executable for debug session, enter C:\\WINDOWS\\SYSTEM32\\RUNDLL32.EXE, assuming C:\\WINDOWS is the Windows directory.

1. For the program arguments, enter **shell32.dll,Control\_RunDLL c:\\windows\\system32\\joy.cpl**. Once again, this assumes that C:\\WINDOWS is your Windows directory. The arguments are case sensitive, and must be entered exactly as shown.

1. Set your breakpoints.

1. From the build menu, select **Start Debug**, then **Go**.

You are now ready to debug your custom property sheet page.
