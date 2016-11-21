---
title: DevCon ListClass
description: Lists all devices in the specified device setup classes. Valid on local and remote computers.
ms.assetid: b642ca5e-5ef1-499f-b8c5-96583a4bd411
keywords: ["DevCon ListClass Driver Development Tools"]
topic_type:
- apiref
api_name:
- DevCon ListClass
api_type:
- NA
---

# DevCon ListClass


Lists all devices in the specified device setup classes. Valid on local and remote computers.

``` syntax
    devcon [/m:\\computer] listclass class [class...] 

   
```

## <span id="ddk_devcon_listclass_tools"></span><span id="DDK_DEVCON_LISTCLASS_TOOLS"></span>Parameters


<span id="________m___computer______"></span><span id="________M___COMPUTER______"></span> **/m:\\\\***computer*   
Runs the command on the specified remote computer. The backslashes are required.

**Note**   To run DevCon commands on a remote computer, the Group Policy setting must allow the Plug and Play service to run on the remote computer. On computers that run Windows Vista and Windows 7, the Group Policy disables remote access to the service by default. On computers that run WDK 8.1 and WDK 8, the remote access is unavailable.

 

<span id="_______class______"></span><span id="_______CLASS______"></span> *class*   
Specifies a device setup class. No equal sign (=) is required.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The **/m** parameter must precede the operation name (**listclass**). Otherwise, DevCon ignores the **/m** parameter and displays the devices on the local computer without returning a syntax error.

Each entry in a setup class display represents one device. The entry consists of the unique instance name and a description of the device in *instance* **:** *description* format.

To find the setup class of a particular device, use the [**DevCon Stack**](devcon-stack.md) operation.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon listclass printers ports
devcon /m:\\Server01 listclass SmartCardReader
```

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

[Example 6: List the devices in a device setup class](devcon-examples.md#ddk_example_6_list_the_devices_in_a_device_setup_class_tools)

[Example 7: List the devices in multiple classes on a remote computer](devcon-examples.md#ddk_example_7_list_the_devices_in_multiple_classes_on_a_remote_compute)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20DevCon%20ListClass%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




