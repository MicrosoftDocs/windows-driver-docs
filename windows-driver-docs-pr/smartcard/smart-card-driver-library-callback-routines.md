---
title: Smart Card Driver Library Callback Routines
description: Smart Card Driver Library Callback Routines
ms.assetid: e536d539-4871-4b1d-bb5a-92a310dfa1e7
keywords: ["IOCTLs WDK smart card", "library callback routines WDK smart card", "callback routines WDK smart card", "ReaderFunction", "vendor-supplied drivers WDK smart card , IOCTL request management"]
---

# Smart Card Driver Library Callback Routines


## <span id="_ntovr_smart_card_driver_library_callback_routines"></span><span id="_NTOVR_SMART_CARD_DRIVER_LIBRARY_CALLBACK_ROUTINES"></span>


The smart card architecture defines a set of standard callback routine types. For details about these routines, see [Smart Card Driver Callbacks](https://msdn.microsoft.com/library/windows/hardware/ff548982).

A reader driver must make these callback routines available for the driver library routine, [**SmartcardDeviceControl (WDM)**](https://msdn.microsoft.com/library/windows/hardware/ff548939), to call by storing pointers to them in the smart card device extension, which is of type [**SMARTCARD\_EXTENSION**](https://msdn.microsoft.com/library/windows/hardware/ff548974). These pointers are stored in an array that is located in the **ReaderFunction** member of SMARTCARD\_EXTENSION structure. Individual callback routines can be identified by a series of constant values, which should be used as indexes into the **ReaderFunction** array.

For instance, if you want [**SmartcardDeviceControl**](https://msdn.microsoft.com/library/windows/hardware/ff548939) to call a callback routine in your reader driver named **DriverCardPower** whenever it finishes processing an [**IOCTL\_SMARTCARD\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff548907) request, you must use the [*RDF\_CARD\_POWER*](https://msdn.microsoft.com/library/windows/hardware/ff548919) constant to initialize the device extension in the following manner:

```
SmartcardExtension->ReaderFunction[RDF_CARD_POWER] = 
DriverCardPower;
```

RDF\_CARD\_POWER is a fixed, system-defined constant that always corresponds to the callback routine that services the IOCTL\_SMARTCARD\_POWER request.

If the member of the **ReaderFunction** array that corresponds to the IOCTL being processed is **NULL**, [**SmartcardDeviceControl**](https://msdn.microsoft.com/library/windows/hardware/ff548939) returns a status of STATUS\_NOT\_SUPPORTED to the reader driver. In some cases, this behavior is useful. If, for example, your driver does not support card ejecting or card swallowing, simply assign the appropriate member of the **ReaderFunction** array to be **NULL**, and **SmartcardDeviceControl** will return STATUS\_NOT\_SUPPORTED whenever that member routine is called.

The following table lists the constants that identify the various types of callback routines. These are the constants that you should use as indexes into the **ReaderFunction** array. The table also provides a brief description of each routine type and indicates whether it is mandatory or optional for a reader driver to implement the routine.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Index</th>
<th align="left">Description of corresponding callback routine</th>
<th align="left">Implementation by the reader driver</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<em>RDF_CARD_POWER</em>](https://msdn.microsoft.com/library/windows/hardware/ff548919)</p></td>
<td align="left"><p>Resets or turns off an inserted smart card</p></td>
<td align="left"><p>Mandatory</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>RDF_CARD_EJECT</em>](https://msdn.microsoft.com/library/windows/hardware/ff548918)</p></td>
<td align="left"><p>Ejects an inserted smart card</p></td>
<td align="left"><p>Optional</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>RDF_CARD_TRACKING</em>](https://msdn.microsoft.com/library/windows/hardware/ff548920)</p></td>
<td align="left"><p>Installs an event handler to track card insertions and removals</p></td>
<td align="left"><p>Mandatory</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>RDF_IOCTL_VENDOR</em>](https://msdn.microsoft.com/library/windows/hardware/ff548921)</p></td>
<td align="left"><p>Performs vendor-specific IOCTL operations</p></td>
<td align="left"><p>Optional</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>RDF_READER_SWALLOW</em>](https://msdn.microsoft.com/library/windows/hardware/ff548922)</p></td>
<td align="left"><p>Does a mechanical swallow</p></td>
<td align="left"><p>Optional</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>RDF_SET_PROTOCOL</em>](https://msdn.microsoft.com/library/windows/hardware/ff548923)</p></td>
<td align="left"><p>Selects a transmission protocol for the card that is in the card reader</p></td>
<td align="left"><p>Mandatory</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<em>RDF_TRANSMIT</em>](https://msdn.microsoft.com/library/windows/hardware/ff548924)</p></td>
<td align="left"><p>Performs data transmissions</p></td>
<td align="left"><p>Mandatory</p></td>
</tr>
</tbody>
</table>

 

When the reader driver calls these routines, it should retrieve the calling parameters from the input buffers, as described in [Smart Card Driver Callbacks](https://msdn.microsoft.com/library/windows/hardware/ff548982). The reader driver should also store the output data in the appropriate buffer areas, as described in the same section.

When any callback routine other than the card-tracking callback routine returns STATUS\_PENDING, the smart card library stops servicing any further calls from the reader driver. (For information about the card-tracking callback routine, see [*RDF\_CARD\_TRACKING*](https://msdn.microsoft.com/library/windows/hardware/ff548920).) If the reader driver attempts to use a driver library routine while the library is in this state, the library routine returns a status of STATUS\_DEVICE\_BUSY. This effectively prevents the reader driver from servicing IOCTL requests from the resource manager, because the reader driver cannot process IOCTL requests if it cannot call [**SmartcardDeviceControl**](https://msdn.microsoft.com/library/windows/hardware/ff548939).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[smartcrd\smartcrd]:%20Smart%20Card%20Driver%20Library%20Callback%20Routines%20%20RELEASE:%20%287/20/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




