---
title: JavaScript API Reference
description: Use the JavaScript API in combination with a Bidi XML file to provide support over a USB connection to a print device.
ms.date: 07/17/2023
---

# JavaScript API Reference

[!include[Print Support Apps](../includes/print-support-apps.md)]

Manufacturers can use the JavaScript API presented here, in combination with a Bidi XML file to provide support for Bidi over a USB connection to a print device.

For more information about USB Bidi communication with a print device, see [USB Bidi Extender](usb-bidi-extender.md).

## Bidi over USB

### getSchemas method

This method handles Bidi GET queries such as \\Printer.Consumables.YellowInk:Level. The JavaScript code is able to make queries to the printer using the USB bus and read responses as they come back.

#### syntax

```javascript
function getSchemas(scriptContext, printerStream, schemaRequests, printerBidiSchemaResponses);
```

#### Parameters (getSchemas method)

*scriptContext*
\[in\] An [**IPrinterScriptContext**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterscriptcontext) object that provides access to relevant property bags.
*printerStream*

\[in\] An [IPrinterScriptableSequentialStream](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterscriptablesequentialstream) object that allows read and write access to the USB bus.
*schemaRequests*

\[in\] Array object containing all of the requested Bidi query strings.
*printerBidiSchemaResponses*

\[out\] Object that the script uses to store all responses to query keys.

#### Return values (getSchemas method)

| Return value | Description |
|---|---|
| 0 | The script completed successfully. |
| 1 | The attached device wasn't ready to provide some requested information. Indicates that the print system should call the function again using any Requery Keys added during processing. |

### setSchema method

This method handles Bidi SET operations. The script can determine the incoming Bidi Schema value to either set data in the device, or perform some action on the device like clean ink heads.

If the device isn't ready to process the specified data, the method can return a value of 1 to indicate the call should be retried after a wait period.

#### Parameters (setSchema method)

*scriptContext*
\[in\] An [**IPrinterScriptContext**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterscriptcontext) object that provides access to relevant property bags.
*printerStream*

\[in\] An [IPrinterScriptableSequentialStream](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterscriptablesequentialstream) object that allows read and write access to the USB bus.
*printerBidiSchemaElement*

\[in\] An [IPrinterBidiSchemaElement](./iprinterbidischemaelement-interface.md) object that contains all the data associated with the Bidi Schema Value to set.

#### Return values (setSchema method)

| Return value | Description |
|---|---|
| 0 | The script completed successfully. |
| 1 | The attached device wasn't ready to provide some requested information. Indicates that the print system should call the function again using the supplied printerBidiSchemaElement. |

### getStatus method

This method is used to obtain unsolicited status from a printer while the device is printing. This function is only called during printing. The device should provide data on the read channel that this script can interpret into Bidi Schema values. Since the write channel to the device is blocked by print data, only unsolicited status is supported here.

This method is called repeatedly during printing. It's expected that the device will only return data if it's available and the script can understand it. If the device doesn't support unsolicited status or there's no need to call this function again, the script should return a value of 2 that will tell the **getStatus** execution thread in USBMon to exit successfully.

#### Parameters (getStatus method)

*scriptContext*
\[in\] An **IPrinterScriptContext** object that provides access to relevant property bags.
*printerStream*

\[in\] An [IPrinterScriptableSequentialStream](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterscriptablesequentialstream) object that allows read access to the USB bus.
*printerBidiSchemaResponses*

\[out\] Object that the script uses to store all responses to query keys.

#### Return values (getStatus method)

| Return value | Description |
|---|---|
| 0 | The script completed successfully. |
| 2 | The attached device no longer supports unsolicited status and this function shouldn't be called again. |

### startPrintJob method

USBMon calls this method during StartDocPort. Calling **startPrintJob** allows the driver to modify the print stream or to implement a host-based request/response protocol that is used while the print device is printing a job. The job context object is passed into the function to allow the manufacturer's JavaScript code to manage job properties and to get access to the persistent data streams. The print data is passed in as a JavaScript array for the JavaScript code to process. **startPrintJob** also provides access to the printer device in the following ways:

- Via the print stream

- Via an object that can return Bidi Schema responses for USBMon to process

#### Syntax (startPrintJob method)

```javascript
function startPrintJob(jobScriptContext, printerStream, printerBidiSchemaResponses);
```

#### Parameters (startPrintJob method)

*jobScriptContext*
\[in\] An [**IPrinterScriptUsbJobContext**](./iprinterscriptusbjobcontext.md) object that gives the manufacturer's JavaScript code access to the job property bag and the persistent data stream(s).
*printerStream*

\[in\] An **IPrinterScriptableSequentialStream** object, that the manufacturer's JavaScript code can use to read and write data to the print device.
*printerBidiSchemaResponses*

\[out\] An [**IPrinterBidiSchemaResponses**](./iprinterbidischemaresponses.md) object that the manufacturer's JavaScript code can use to return any Bidi Schema value changes/updates.

#### Return values (startPrintJob method)

| Return value | Description |
|---|---|
| 0 | Success. |
| 1 | Failure – Clean up the Job Context object and return an error code to the print spooler. |

### writePrintData method

USBMon calls this method during writePort. Calling **writePrintData** allows the driver to modify the print stream or to implement a host-based request/response protocol that is used while the print device is printing a job. The job context object is passed into the method to allow the manufacturer's JavaScript code to manage job properties and to get access to the persistent data streams. The print data is passed in as a JavaScript array for the JavaScript code to process. **writePrintData** also provides access to the printer device in the following ways:

- Via the print stream

- Via an object that can return Bidi Schema responses for USBMon to process

```javascript
function writePrintData(jobScriptContext, writePrintDataProgress, printData, printerStream, printerBidiSchemaResponses);
```

#### Parameters (writePrintData method)

*jobScriptContext*
\[in\] An **IPrinterScriptUsbJobContext** object that gives the manufacturer's JavaScript code access to the job property bag and the persistent data stream(s).
*writePrintDataProgress*

\[in\] An **IPrinterScriptableSequentialStream** object that the manufacturer's JavaScript code can use to read and write data to the print device.
*printData*

\[in\] An **IDispatch** object, a JavaScript array of the current print data. The *printData* parameter allows the JavaScript code to manipulate the data before either caching it to one of the data streams in *jobScriptContext* or sending it to the printer via *printerStream*.
*printerStream*

\[in\] An **IPrinterScriptableSequentialStream** object that the manufacturer's JavaScript code can use to read and write data to the print device.
*printerBidiSchemaResponses*

\[out\] An **IPrinterBidiSchemaResponses** object that the manufacturer's JavaScript code can use to return any Bidi Schema value changes or updates.

#### Return values (writePrintData method)

| Return value | Description |
|--|--|
| 0 | Success. The number of bytes processed from the print data stream (*printData*) is returned via *writePrintDataProgress*. |
| 1 | Failure – Return an error code to the print spooler. |
| 2 | Retry - Process any Bidi Schema updates (including Bidi Events) in *printerBidiSchemaResponses*, and then call the JavaScript function again to allow the manufacturer's code to continue processing the data. The number of bytes processed from the print data stream (*printData*) is returned via *writePrintDataProgress*. |
| 3 | DeviceBusy – The device communication channel isn't accepting data at this time. This doesn't indicate a failure. USBMon should inform the spooler that the device is busy, and then call the function again at a later time. The number of bytes processed from the print data stream (*printData*) is returned via *writePrintDataProgress*. |
| 4 | AbortTheJob – The device can't continue processing the job, or the user has canceled the job using the front panel of the print device. When USBMon receives the message to abort a print job, it passes the information to the print spooler to abort the job, before returning. |

### endPrintJob method

USBMon calls this method during endDocPort. Calling **endPrintJob** allows the driver to modify the print stream or to implement a host-based request/response protocol that is used while the print device is printing a job. The job context object is passed into the method to allow the manufacturer's JavaScript code to:

- Finish processing any print data that persisted

- Access the printer device via the print stream

- Access an object that can pass Bidi Schema responses for USBMon to process

```javascript
function endPrintJob(jobScriptContext, printerStream, printerBidiSchemaResponses);
```

#### Parameters (endPrintJob method)

*jobScriptContext*
\[in\] An IPrinterScriptUsbJobContext object that gives the manufacturer's JavaScript code access to the job property bag and the persistent data stream(s).
*printerStream*

\[in\] An IPrinterScriptableSequentialStream object that the manufacturer's JavaScript code can use to read and write data to the print device.
*printerBidiSchemaResponses*

\[out\] An IPrinterBidiSchemaResponses object that the manufacturer's JavaScript code can use to return any Bidi Schema value changes or updates.

#### Return values (endPrintJob method)

| Return value | Description |
|---|---|
| 0 | Success – Clean up the Job Context object and return success to the print spooler. |
| 1 | Failure – Clean up the Job Context object and return an error code to the print spooler. |
| 2 | Retry - Process any Bidi Schema updates (including Bidi Events) in *printerBidiSchemaResponses*, and then call the JavaScript function again to allow the manufacturer's JavaScript code to continue processing the data. |

## Bidi over secondary USB

If the device supports a secondary USB interface, then the device can use the **getSchemas** and **setSchema** methods described in the preceding sections, in addition to the **requestStatus** method.

### requestStatus method

This method is called instead of **getStatus**, if the **BidiUSBStatusInterface** directive has been specified in the v4 driver's manifest file. **requestStatus** is used to obtain status from a print device while the device is printing.

The following diagram provides an overview of the USB Bidi extension architecture, showing the scenario where the **BidiUSBStatusInterface** directive has been specified and communication is therefore routed over an alternate USB interface.

![usb bidi extender architecture with requeststatus method.](images/usbbidiext-arch2.png)

This method is called repeatedly during printing. It's expected that the device will only return data if it's available and the script can understand it. If the device doesn't support solicited status or there's no need to call this method again, the script should return a value of 2 that will tell the **getStatus** execution thread in USBMon to exit successfully.

#### Parameters (requestStatus method)

*scriptContext*
\[in\] An **IPrinterScriptContext** object that provides access to relevant property bags.
*printerStream*

\[in\] An **IPrinterScriptableSequentialStream** object that allows read and write access to the USB bus.
*printerBidiSchemaResponses*

\[out\] Object that the script uses to store all responses to query keys.

#### Return values (requestStatus method)

| Return value | Description |
|---|---|
| 0 | The script completed successfully. |
| 2 | The attached device no longer supports solicited status and this function shouldn't be called again. |

## Related articles

[**IPrinterScriptContext**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterscriptcontext)  

[IPrinterScriptableSequentialStream](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterscriptablesequentialstream)  

[USB Bidi Extender](usb-bidi-extender.md)
