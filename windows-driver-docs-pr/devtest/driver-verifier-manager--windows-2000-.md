---
title: Driver Verifier Manager (Windows 2000)
description: Driver Verifier Manager (Windows 2000)
ms.assetid: d1266d2d-2388-472d-a1c4-875ed24913d4
keywords: ["Driver Verifier Manager", "Verifier utility"]
---

# Driver Verifier Manager (Windows 2000)


## <span id="ddk_driver_verifier_manager_windows_2000__tools"></span><span id="DDK_DRIVER_VERIFIER_MANAGER_WINDOWS_2000__TOOLS"></span>


The Windows 2000 version of Driver Verifier Manager has five separate panels:

1.  The **Driver Status** screen displays which drivers are loaded and are being verified, and which Driver Verifier options are active. See [Viewing Driver Verifier Settings](viewing-driver-verifier-settings.md) for details.

2.  The **Global Counters** screen displays statistics related to Driver Verifier's actions. Although some of these statistics are related to certain Driver Verifier options, these statistics will be displayed regardless of which options are active. See [Monitoring Global Counters](monitoring-global-counters.md) for details.

3.  The **Pool Tracking** screen displays information about pool allocations. See [Monitoring Individual Counters](monitoring-individual-counters.md) for details.

4.  The **Settings** screen is used to activate and configure Driver Verifier's actions. Changes made from this screen take effect after the next boot. See [Selecting Driver Verifier Options](selecting-driver-verifier-options.md) and [Selecting Drivers to be Verified](selecting-drivers-to-be-verified.md) for details.

5.  The **Volatile Settings** screen is used to alter Driver Verifier's volatile actions. Changes made from this screen take effect immediately. See [Using Volatile Settings](using-volatile-settings.md) for details.

Several screens have a **Refresh Frequency** section on them. This is used to control how often the information displayed on that screen is updated. **Low**, **Medium**, and **High** instruct Driver Verifier to refresh the screen every 1, 5, or 10 seconds, respectively. **Manual** disables automatic updating. The **Refresh Now** button causes the screen to be refreshed immediately.

To exit Driver Verifier Manager, use the **Exit** button. If you have made any changes and have not pressed the corresponding **Apply** button, you will be asked if you wish to save your changes.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Driver%20Verifier%20Manager%20%28Windows%202000%29%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




