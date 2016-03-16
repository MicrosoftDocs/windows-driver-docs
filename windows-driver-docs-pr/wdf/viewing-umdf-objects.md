---
title: Viewing UMDF Objects
description: This topic describes how you can use the Wudfext.dll debugger extensions to view information about objects used by a User Mode Driver Framework (UMDF) version 1 driver.
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 36d0d604-3ed1-4ca7-b5bd-207942ecfc1e
keywords: ["debugging scenarios WDK UMDF viewing UMDF objects", "UMDF WDK debugging scenarios viewing UMDF objects", "UMDF WDK viewing UMDF objects"]
---

# Viewing UMDF Objects


This topic describes how you can use the Wudfext.dll debugger extensions to view information about objects used by a User-Mode Driver Framework (UMDF) version 1 driver.

Starting with UMDF version 2, you should instead use the Wdfkd.dll debugger extensions. For more info, see [Windows Driver Framework Extensions (Wdfkd.dll)](https://msdn.microsoft.com/library/windows/hardware/ff551876).

You can perform the following steps to view information about UMDF version 1 objects:

1.  Use one of the following UMDF debugger extensions to view device stacks that are in the host process:
    -   **!wudfext.umdevstacks**
    -   **!wudfext.umdevstack** as shown in the following example:

        **!wudfext.umdevstack &lt;dev-stack-addr&gt;**

        The information includes driver objects and device objects for each driver. Currently, UMDF allows only one device stack in a host process so there is no difference between the outputs of these two extensions.

2.  View the complete object tree by using the **!wudfext.wudfobject** UMDF debugger extension, as in the following example:

    **!wudfext.wudfobject &lt;IWDFDriver\*&gt; 1**

3.  Use the **!wudfext.wudfdevice** UMDF debugger extension as shown in the following example to determine the Plug and Play (PnP) and power-management state of the device:

    **!wudfext.wudfdevice &lt;IWDFDevice\*&gt;**

4.  Perform the following steps to determine the queues that are associated with the device:
    1.  Use the **!wudfext.wudfdevicequeues** UMDF debugger extension to view the queues that are associated with the device. This extension shows queue properties, queue state, and driver-owned requests.
    2.  Use the **!wudfext.wudfqueue** UMDF debugger extension as shown in the following example to obtain information about each queue:

        **!wudfext.wudfqueue &lt;IWDFIoQueue\*&gt;**

5.  Use the **!wudfext.wudfrequest** UMDF debugger extension to obtain information about a particular request. This information includes the underlying user-mode I/O request packet (IRP). From the user-mode IRP information, you can determine where the request is currently being processed in the stack. You can also use the **!wudfext.umirp** UMDF debugger extension to obtain this user-mode IRP information.

6.  Determine all I/O targets by:

    1.  Using the **!wudfext.wudfobject** UMDF debugger extension to view the child objects of the device object. I/O target objects are child objects of the device object.
    2.  Using the **!wudfext.wudfiotarget** UMDF debugger extension as shown in the following example to view information about each I/O target object:

        **!wudfext.wudfiotarget &lt;IWDFTarget\*&gt;**

        This extension shows the target's state and the list of sent requests.

    There is currently no UMDF debugger extension that allows you to view all I/O targets.

7.  Use the following UMDF debugger extensions to view information about file objects:

    <a href="" id="-wudfext-wudfrequest-or--wudfext-umirp"></a>**!wudfext.wudfrequest** or **!wudfext.umirp**  
    Use the **!wudfext.wudfrequest** or the **!wudfext.umirp** UMDF debugger extension to view files that are child objects of device objects.

    <a href="" id="-wudfext-wudffile"></a>**!wudfext.wudffile**  
    Use the **!wudfext.wudffile** UMDF debugger extension as shown in the following example to view information about a framework file:

    **!wudfext.wudffile &lt;IWDFFile\*&gt;**

    <a href="" id="-wudfext-umfile"></a>**!wudfext.umfile**  
    Use the **!wudfext.umfile** UMDF debugger extension as shown in the following example to view information about a UMDF intra-stack file (that is, a file object that a driver in the stack created as opposed to a file object that was created by an application or by a driver in another stack):

    **!wudfext.umfile &lt;addr&gt;**

    In some cases, there might not be a corresponding framework file, and user-mode IRP information might include a UMDF intra-stack file.

    Information that **!wudfext.umfile** displays includes any IRPs that are queued to the UMDF intra-stack file. Only driver-created files track user-mode IRPs that are queued to those files. For application-created files, the I/O manager tracks the kernel-mode IRPs.

    <a href="" id="-wudfext-umdevstacks-and--wudfext-umdevstack"></a>**!wudfext.umdevstacks** and **!wudfext.umdevstack**  
    Use the output from the **!wudfext.umdevstacks** and **!wudfext.umdevstack** UMDF debugger extensions to view outstanding UMDF intra-stack files that correspond to driver-created files.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Viewing%20UMDF%20Objects%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




