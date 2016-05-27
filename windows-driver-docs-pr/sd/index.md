---
Description: SD Bus Driver Design Guide
MS-HAID:
- 'sd\_dg\_d61cae93-a8a3-4360-b138-04a705a59ff9.xml'
- 'SD.sd\_bus\_design\_guide'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: SD Bus Driver Design Guide
---

# SD Bus Driver Design Guide


## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[SD Card Driver Stack](buses.sd_card_driver_stack)</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>[Opening, Initializing and Closing an SD Card Bus Interface](buses.opening__initializing_and_closing_an_sd_card_bus_interface)</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>[Handling SD Card Interrupts](buses.handling_sd_card_interrupts)</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>[SD Card Requests](buses.sd_card_requests)</p></td>
<td></td>
</tr>
</tbody>
</table>

 

## SD Card Hardware Identifiers


For information about Secure Digital (SD) device identification strings, see [Identifiers for Secure Digital (SD) Devices](devinst.identifiers_for_secure_digital__sd__devices).

## Restrictions on SD Card Drivers


Certain restrictions apply to Secure Digital (SD) card device drivers that manage a function on an SD combo or multifunction card. The driver stacks for the various card functions on a multifunction card must operate independently of one another. To ensure this independence, the bus driver rejects the following operations:

-   SD commands that change the device state, such as SELECT\_CARD.

-   SD I/O commands that specify function zero but are outside the range of the address specified in the function basic register (FBR).

-   SD I/O commands that specify a function number of a different device stack.

SD device drivers can manage the host controller's common register set and the state of the device by calling [**SdBusSubmitRequest**](buses.sdbussubmitrequest) with function requests of type SDRF\_GET\_PROPERTY and SDRF\_SET\_PROPERTY. For a description of these function request types, see [**SD\_REQUEST\_FUNCTION**](buses.sd_request_function).

## SD Bus Sample


This is a sample for a functional Secure Digital (SD) IO driver. The driver is written using the Kernel Mode Driver Framework. It is a driver for a generic mars development board that implements the SDIO protocol without additional functionality.

Download the [Storage SDIO driver sample](http://go.microsoft.com/fwlink/p/?LinkId=617953) from GitHub.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BSD\buses%5D:%20SD%20Bus%20Driver%20Design%20Guide%20%20RELEASE:%20%285/27/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



