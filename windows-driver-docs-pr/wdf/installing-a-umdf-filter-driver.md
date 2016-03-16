---
title: Installing a UMDF Filter Driver
description: A filter driver can support a specific device or all devices in a setup class.
ms.assetid: AE6D4E36-B758-451A-983E-6F0D7ADFD7A7
---

# Installing a UMDF Filter Driver


A filter driver can support a specific device or all devices in a setup class. A lower filter driver attaches below a device's function driver, while an upper filter attaches above a device's function driver.

This topic describes how to install and configure a User-Mode Driver Framework (UMDF) device-specific (upper or lower) filter driver. You cannot use UMDF to write a class filter driver. This topic applies to both UMDF versions 1 and 2.

As you structure your device stack, keep in mind that the framework currently supports only one contiguous block of UMDF drivers per stack. Also, you cannot install UMDF version 1 and version 2 drivers in the same device stack.

**How to install and configure your driver**

1.  A UMDF 1 filter driver should call [**IWDFDeviceInitialize::SetFilter**](https://msdn.microsoft.com/library/windows/hardware/ff556985) from the its [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) callback function. Starting in UMDF version 2, your driver instead calls [**WdfFdoInitSetFilter**](https://msdn.microsoft.com/library/windows/hardware/ff547273).

2.  In addition to any UMDF-specific directives your driver may specify, you must specify the **UmdfService** and **UmdfServiceOrder** directives. In this topic, we'll specify an upper filter driver:

    <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>[&lt;mydriver&gt;_Install.NT.Wdf]
    UmdfService=UMDFFunction,WUDFFuncDriver_Install
    UmdfService=UMDFFilter,UMDFFilter_Install
    UmdfServiceOrder=UMDFFunction,UMDFFilter</code></pre></td>
    </tr>
    </tbody>
    </table>

    The drivers are added to the device stack in the order that they are listed in the **UmdfServiceOrder** entry. The first parameter specifies the lowest UMDF driver in the device stack. To install a lower filter driver, simply reverse the arguments for **UmdfServiceOrder**.

    For more info about these and other UMDF-specific INF directives, see [Specifying WDF Directives in INF Files](specifying-wdf-directives-in-inf-files.md).

3.  If your driver's device stack contains only UMDF drivers, skip this step.

    If your driver's device stack contains any drivers that are not UMDF, your INF file must include an **AddReg** section that specifies the reflector as an upper filter driver:

    <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>[&lt;mydriver&gt;_Device_AddReg]
    ; Load the redirector as an upperfilter on this specific device.
    ; 0x00010008 - FLG_ADDREG_TYPE_MULTI_SZ | FLG_ADDREG_APPEND
    HKR,,&quot;UpperFilters&quot;,0x00010008,&quot;WUDFRd&quot; </code></pre></td>
    </tr>
    </tbody>
    </table>

4.  After your driver is loaded as an upper filter, it is responsible for forwarding I/O requests to the next driver in the stack. To illustrate, consider a simple pass-through driver (UMDF version 1) that is above a KMDF function driver.

    First, retrieve the interface of the default I/O target (next driver in the stack). Then, format and send the request. The simplest scenario would look like this:

    <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>IWDFIoTarget * kmdfIoTarget = NULL;
        
        this-&gt;GetFxDevice()-&gt;GetDefaultIoTarget (&amp;kmdfIoTarget);

        Request-&gt;FormatUsingCurrentType();

        hr = Request-&gt;Send (
            kmdfIoTarget, 
            0,  // 0 Submits Asynchronous else use WDF_REQUEST_SEND_OPTION_SYNCHRONOUS
            0);</code></pre></td>
    </tr>
    </tbody>
    </table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Installing%20a%20UMDF%20Filter%20Driver%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




