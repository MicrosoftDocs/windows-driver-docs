---
Description: 'The User Mode Driver Framework (UMDF) requires that drivers support the IPnpCallback interface for Plug and Play (PnP) operations and the IPnpCallbackSelfManagedIo interface for power-management operations.'
MS-HAID: 'wpddk.supporting\_plug\_and\_play\_\_pnp\_'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: 'Supporting Plug and Play (PnP) and Power Management'
---

# Supporting Plug and Play (PnP) and Power Management


The User Mode Driver Framework (UMDF) requires that drivers support the [**IPnpCallback**](https://msdn.microsoft.com/library/windows/hardware/ff556762) interface for Plug and Play (PnP) operations and the [**IPnpCallbackSelfManagedIo**](https://msdn.microsoft.com/library/windows/hardware/ff556776) interface for power-management operations.

The first interface, **IPnpCallback** supports the methods invoked when a user plugs-in, or unplugs, their device. The second interface, **IPnpCallbackSelfManagedIo** supports the methods invoked when a device enters low-power state, or, returns to its working state.

Because all but one of the WPD samples emulate hardware, the methods for these interfaces perform no meaningful work and return immediately.

The one exception is the WpdBasicHardwareDriver sample. Because this driver supports actual hardware, it contains working code for two methods in the **IPnpCallback** interface. The two methods supported by this sample are [**IPnpCallback::OnD0Entry**](https://msdn.microsoft.com/library/windows/hardware/ff556799) and [**IPnpCallback::OnD0Exit**](https://msdn.microsoft.com/library/windows/hardware/ff556803). The first method retrieves a pointer to the I/O Target that the sample driver uses to forward I/O requests to the kernel-mode RS232 driver. After retrieving this pointer, the **IPnpCallback::OnDOEntry** method starts the I/O target. The second method, **IPnpCallback::OnD0Exit** retrieves a pointer to the I/O Target and then stops it.

If your driver supports hardware, you'll want to add support for one, or both, of these interfaces. For a complete description of PnP and Power-Management in user-mode device drivers, refer to the [PnP and Power Management Scenarios in UMDF](https://msdn.microsoft.com/library/windows/hardware/ff560452)topic on MSDN.

## <span id="related_topics"></span>Related topics


[**IPnpCallback**](https://msdn.microsoft.com/library/windows/hardware/ff556762)

[**IPnpCallback::OnD0Entry**](https://msdn.microsoft.com/library/windows/hardware/ff556799)

[**IPnpCallback::OnD0Exit**](https://msdn.microsoft.com/library/windows/hardware/ff556803)

[**IPnpCallbackSelfManagedIo**](https://msdn.microsoft.com/library/windows/hardware/ff556776)

[PnP and Power Management Scenarios in UMDF](https://msdn.microsoft.com/library/windows/hardware/ff560452)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Supporting%20Plug%20and%20Play%20%28PnP%29%20and%20Power%20Management%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




