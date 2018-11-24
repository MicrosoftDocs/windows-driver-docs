---
title: Porting a Driver from UMDF 1 to UMDF 2
description: This topic describes how to port a User-Mode Driver Framework (UMDF) 1 driver to UMDF 2.
ms.assetid: 99D20B4C-17C4-42AC-B4D9-F5FD64E10723
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting a Driver from UMDF 1 to UMDF 2


This topic describes how to port a User-Mode Driver Framework (UMDF) 1 driver to UMDF 2. You can start with a UMDF 1 driver that uses Sources/Dirs files (not a Visual Studio project), or you can convert a UMDF 1 driver that is contained in a Visual Studio project. The result will be a UMDF 2 driver project in Visual Studio. UMDF 2 drivers run on both Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) and Windows 10 Mobile.

The Echo driver sample is an example of a driver that has been ported from UMDF 1 to UMDF 2.

-   [Echo Sample (UMDF Version 1)](http://go.microsoft.com/fwlink/p/?LinkId=617707)
-   [Echo Sample (UMDF Version 2)](http://go.microsoft.com/fwlink/p/?LinkId=617708)

## Getting Started


To start, open a new driver project in Visual Studio. Select the **Visual C++-&gt;Windows Driver-&gt;WDF-&gt;User Mode Driver (UMDF 2)** template. Visual Studio opens a partially populated template that includes stubs for the callback functions that your driver must implement. This new driver project will be the foundation of your UMDF 2 driver. Use the UMDF 2 Echo sample as a guide to the type of code you should introduce.

Next, review your existing UMDF 1 driver code and determine object mappings. Each COM object in UMDF 1 has a corresponding WDF object in UMDF 2. For example, the **IWDFDevice** interface maps to the WDF device object, which is represented by a WDFDEVICE handle. Nearly all framework-supplied interface methods in UMDF 1 have corresponding methods in UMDF 2. For example, [**IWDFDevice::GetDefaultIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff558830) maps to [**WdfDeviceGetDefaultQueue**](https://msdn.microsoft.com/library/windows/hardware/ff545965).

Similarly, driver-supplied callback functions have equivalents in the two versions. In UMDF 1, the naming convention for driver-supplied interfaces (except for **IDriverEntry**) is *I*Object*Callback*Xxx<strong>, while in UMDF 2 the naming convention for driver-supplied routines is *Evt*ObjectXxx</strong>. For example, the [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) callback method maps to [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693).

Your driver implements callback functions in both UMDF 1 and 2, but the way that the driver supplies pointers to its callbacks differs. In UMDF 1, the driver implements callback methods as members of driver-supplied interfaces. The driver registers these interfaces with the framework when it creates framework objects, for example by calling [**IWDFDriver::CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff558899).

In UMDF 2, the driver provides pointers to driver-supplied callback functions in configuration structures such as [**WDF\_DRIVER\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551300) and [**WDF\_IO\_QUEUE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552359).

## Managing Object Lifetime


Drivers that use UMDF 1 must implement reference counting in order to determine when it is safe to delete objects. Because the framework tracks object references on the driver's behalf, a UMDF 2 driver does not need to count references.

In UMDF 2, each framework object has a default parent object. When a parent object is deleted, the framework deletes associated child objects. When your driver calls an object creation method such as [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926), it can accept the default parent, or it can specify a custom parent in a [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure. For a list of framework objects and their default parent objects, see [Summary of Framework Objects](summary-of-framework-objects.md).

## Driver Initialization


A UMDF 1 driver implements the [**IDriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff554885) interface. In its [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) callback method, the driver typically:

-   Creates and initializes an instance of the device callback object.
-   Creates the new framework device object by calling [**IWDFDriver::CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff558899).
-   Sets up the device's queues and their corresponding callback objects.
-   Creates an instance of a device interface class by calling [**IWDFDevice::CreateDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff557016).

A UMDF 2 driver implements [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff540807) and [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693). In its **DriverEntry** routine, a UMDF 2 driver typically calls [**WDF\_DRIVER\_CONFIG\_INIT**](https://msdn.microsoft.com/library/windows/hardware/ff551302) to initialize the driver's [**WDF\_DRIVER\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551300) structure. Then it passes this structure to [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175).

In its [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) function, the driver might do some of the following:

-   Fill in the [WDFDEVICE\_INIT](https://msdn.microsoft.com/library/windows/hardware/ff546951) structure, which supplies information that is used to create the device object. For more information about using WDFDEVICE\_INIT, see [Creating a Framework Device Object](creating-a-framework-device-object.md).
-   Set up the device object’s context area. For information about allocating and accessing context space for framework objects, see [Framework Object Context Space](framework-object-context-space.md).
-   [Create the device object](creating-a-framework-device-object.md).
-   Specify [request handlers](request-handlers.md) for the device object.
-   [Create I/O queues](creating-i-o-queues.md).
-   [Create device interfaces](using-device-interfaces.md).
-   Set [device idle policy](supporting-idle-power-down.md) and [wake settings](supporting-system-wake-up.md), if the device object owns power policy.
-   [Create interrupt objects](creating-an-interrupt-object.md), if the hardware supports interrupts.

## Installing your driver


When you create a new driver project in Visual Studio, the new project contains an .inx file. When you build your driver, Visual Studio compiles your .inx file into an INF file that can be used as part of a driver package.

While an INF file for a UMDF 1 driver must include a driver class ID, a DriverCLSID is not required in an INF file for a UMDF 2 driver.

Also, although a UMDF 1 driver must reference the co-installer in its INF file, no constaller reference is required in a UMDF 2 INF file. Though a coinstaller reference can appear in an INF file for a UMDF 2 driver, one is not required.

## Storing Device Context


In UMDF 1, the driver usually stores device context in a driver-created callback object, for example by specifying private members of the device callback object class. Alternatively, a UMDF 1 driver can call the [**IWDFObject::AssignContext**](https://msdn.microsoft.com/library/windows/hardware/ff560208) method to register context on a framework object.

In UMDF 2, the framework allocates context space based on the optional [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure that the driver provides when it calls an object creation method. After calling an object's create method, a driver can call [**WdfObjectAllocateContext**](https://msdn.microsoft.com/library/windows/hardware/ff548723) one or more times to allocate additional context space to a specific object. For the steps a UMDF 2 driver should use to define a context structure and accessor method, see [Framework Object Context Space](framework-object-context-space.md).

## Debugging your driver


To debug a UMDF 2 driver, you'll use extensions in Wdfkd.dll instead of Wudfext.dll. For more info about extensions in Wudfext.dll, see [Summary of Debugger Extensions in Wdfkd.dll](debugger-extensions-for-kmdf-drivers.md).

In UMDF 2, you can also get additional driver debugging information through the Inflight Trace Recorder (IFR), as described in [Using Inflight Trace Recorder in KMDF and UMDF 2 Drivers](using-wpp-software-tracing-in-kmdf-and-umdf-2-drivers.md). Also, you can use the framework's own *In-flight Recorder* (IFR). See [Using the Framework's Event Logger](using-the-framework-s-event-logger.md).

## Related topics


[Getting Started with UMDF](getting-started-with-umdf-version-2.md)

[Framework Object Context Space](framework-object-context-space.md)

[UMDF Version History](umdf-version-history.md)

[Framework Objects](framework-objects.md)

 

 






