---
title: wdfkd.wdfumdownirp
description: The wdfkd.wdfumdownirp extension displays the kernel-mode I/O request packet (IRP) that is associated with a specified user-mode IRP.
ms.assetid: 98DFF193-950A-46CF-875E-B2907743F5D4
keywords: ["wdfkd.wdfumdownirp Windows Debugging"]
topic_type:
- apiref
api_name:
- wdfkd.wdfumdownirp
api_type:
- NA
---

# !wdfkd.wdfumdownirp


The **!wdfkd.wdfumdownirp** extension displays the kernel-mode I/O request packet (IRP) that is associated with a specified user-mode IRP. This command is used in two steps. See Remarks.

``` syntax
!wdfkd.wdfumdownirp UmIrp [FileObject] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______UmIrp______"></span><span id="_______umirp______"></span><span id="_______UMIRP______"></span> *UmIrp*   
Specifies the address of a user mode IRP. You can use [**!wdfkd.wdfumirps**](-wdfkd-wdfumirps.md) to get the addresses of UM IRPs in the [implicit process](controlling-threads-and-processes.md).

<span id="_______FileObject______"></span><span id="_______fileobject______"></span><span id="_______FILEOBJECT______"></span> *FileObject*   
Specifies the address of a **\_FILE\_OBJECT** structure. For information about how to get this address, see Remarks.

## <span id="DLL"></span><span id="dll"></span>DLL


Wdfkd.dll

## <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks


UMDF 2

## <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information


For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

You can use this command in a kernel-mode debugging session or in a user-mode debugging session that is attached to the UMDF host process (wudfhost.exe).

To use this command, follow these steps:

1.  Enter this command, passing only the address a user-mode IRP. The command displays a handle.
2.  Pass the displayed handle to the [**!handle**](-handle.md) command. In the output of **!handle**, find the address of a **\_FILE\_OBJECT** structure.
3.  Enter this command again, passing both the address of the user-mode IRP and the address of the **\_FILE\_OBJECT** structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!wdfkd.wdfumdownirp%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




