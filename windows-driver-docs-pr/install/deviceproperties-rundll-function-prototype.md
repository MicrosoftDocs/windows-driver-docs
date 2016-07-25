---
title: DeviceProperties\_RunDLL Function Prototype
description: DeviceProperties\_RunDLL Function Prototype
ms.assetid: 15c93f6d-56e7-4872-a94b-0c948e2cd76f
keywords: ["device properties dialog box WDK device installations", "invoking device properties dialog box", "DeviceProperties_RunDLL WDK device installations", "machine-name-parameter field WDK device installations", "device-instance-ID-parameter field WDK device inst"]
---

# DeviceProperties\_RunDLL Function Prototype


The DeviceProperties\_RunDLL function opens the device properties dialog box for a specified device that is installed on a local or remote computer.

```
void DeviceProperties_RunDLL(
  HWND       hwndStub,
  HINSTANCE  hAppInstance,
  LPCTSTR    lpCmdLine,
  int        nCmdShow
  );
```

### Parameters

<a href="" id="hwndstub"></a>*hwndStub*  
A handle to the window in which to display the user interface items that DeviceProperties\_RunDLL creates.

<a href="" id="happinstance"></a>*hAppInstance*  
This parameter is not used to invoke a device properties dialog box and should be set to **NULL**.

<a href="" id="lpcmdline"></a>*lpCmdLine*  
A pointer to a constant NULL-terminated command-line string that contains a *machine-name-parameter* field followed by a *device-instance-ID-parameter* field in the following format:

*machine-name-parameter device-instance-ID-parameter*

<a href="" id="machine-name-parameter"></a>*machine-name-parameter*  
The *machine-name-parameter* field supplies the name of the machine that is associated with the device that is specified by the *device-instance-ID-parameter* field. The format of the *machine-name-parameter* field is **/MachineName** **** *machine-name*, where **/MachineName** indicates that *machine-name* supplies a computer name. For more information about the *machine-name-parameter* field, see the Remarks section.

<a href="" id="device-instance-id-parameter"></a>*device-instance-ID-parameter*  
The *device-instance-ID-parameter* field supplies a [device instance identifier](device-instance-ids.md) of the device for which to display a device properties dialog box. The format of *device-instance-ID-parameter* field is **/DeviceId** **** *device-instance-ID*, where **/DeviceId** indicates that *device-instance-ID* supplies a device instance identifier. The *device-instance-ID-parameter* field is required.

<a href="" id="ncmdshow"></a>*nCmdShow*  
This parameter is not used to invoke a device properties dialog box and should be set to **NULL**.

### Return Value

None

### Headers

DeviceProperties\_RunDLL is not declared in a public header and can only be invoked indirectly by programmatically obtaining a pointer to the function or by using rundll32.

### <a href="" id="comments"></a>Remarks

On Windows XP, the *machine-name-parameter* field is required only for a remote computer, and, if the *machine-name-parameter* field is not supplied, the local computer is used by default. On Windows 2000, the *machine-name-parameter* field is required for a local computer or a remote computer. To specify a local computer, set *machine-name* in the *machine-name-parameter* field to a pair of quotation marks (""). If the machine is a remote computer, set *machine-name* to a valid computer name. A valid computer name must include a prefix that consists of a pair of backslashes(\\\) followed by the machine name.

The following are examples of command-line strings:

-   (Windows XP and later) Specifying the local computer is optional, in which case the command-line string is required to include only the device instance identifier. For example, the following command-line specifies the local computer by default and the device instance identifier "root\\system\\0000".
    ```
    /DeviceId root\system\0000
    ```

-   (Windows 2000 and later) The following command-line string supplies the remote computer name "\\\\RemoteMachineAbc" and the device instance identifier "root\\system\\0000".
    ```
    /MachineName \\RemoteMachineAbc /DeviceId root\system\0000
    ```

-   (Windows 2000 and later) The following command-line string specifies a local computer, which is specified by a pair of quotation marks (""), and supplies the device instance identifier "root\\system\\0000".
    ```
    /MachineName "" /DeviceId root\system\0000
    ```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DeviceProperties_RunDLL%20Function%20Prototype%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




