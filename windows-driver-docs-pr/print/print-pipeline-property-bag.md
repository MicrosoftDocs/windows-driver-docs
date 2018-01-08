---
title: Print Pipeline Property Bag
description: The print pipeline property bag is used to pass information between filters in the filter pipeline.Property nameSymbolic nameProperty typeDescriptionPrinterNameXPS\_FP\_PRINTER\_NAMEVT\_BSTRThe printer name.ProgressReportXPS\_FP\_PROGRESS\_REPORTVT\_UNKNOWNA pointer to an IUnknown interface. Call QueryInterface to obtain a pointer to the IPrintPipelineProgressReport interface.PrinterHandleXPS\_FP\_PRINTER\_HANDLE VT\_BYREFThe printer handle. The filter should not close this handle.PerUserPrintTicketXPS\_FP\_USER\_PRINT\_TICKETVT\_UNKNOWNA pointer to an IUnknown interface. Call QueryInterface to obtain a pointer to the IPrintReadStreamFactory interface.UserSecurityTokenXPS\_FP\_USER\_TOKENVT\_BYREFA handle that the filter can use to impersonate the user account that submitted the print job.PrintJobIdXPS\_FP\_JOB\_IDVT\_UI4The print job identification number.PrintClassFactoryXPS\_FP\_PRINT\_CLASS\_FACTORYVT\_UNKNOWNA pointer to an IUnknown interface. Call QueryInterface to obtain a pointer to the IPrintClassObjectFactory interface.IPrintCoreHelper(There is no symbolic name for this property name.)VT\_UNKNOWNA pointer to an IUnknown interface. Call QueryInterface to obtain a pointer to the IPrintCoreHelper interface.Note that this property is only available in XPSDrv printer drivers that use the unidrvui.dll as the configuration UI DLL.PrintDeviceCapabilitiesXPS\_FP\_PRINTDEVICECAPABILITIES VT\_UNKNOWNA pointer to an IUnknown interface. Call QueryInterface to obtain a pointer to the IPrintReadStreamFactory interface.Allows XPS rendering filters to retrieve PrintDeviceCapabilities XML files from the Print filter pipeline property bag. �
MS-HAID:
- 'filterpipeline\_f3fbd165-3f72-41cc-91b8-aa8b36823da9.xml'
- 'print.print\_pipeline\_property\_bag'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5a0fb200-a2c2-41f0-8dcf-6eb3361c148e
keywords: ["Print Pipeline Property Bag Print Devices"]
topic_type:
- apiref
api_name:
- Print Pipeline Property Bag
api_type:
- NA
---

# Print Pipeline Property Bag


The print pipeline property bag is used to pass information between filters in the filter pipeline.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Property name</th>
<th>Symbolic name</th>
<th>Property type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PrinterName</p></td>
<td><p>XPS_FP_PRINTER_NAME</p></td>
<td><p>VT_BSTR</p></td>
<td><p>The printer name.</p></td>
</tr>
<tr class="even">
<td><p>ProgressReport</p></td>
<td><p>XPS_FP_PROGRESS_REPORT</p></td>
<td><p>VT_UNKNOWN</p></td>
<td><p>A pointer to an <strong>IUnknown</strong> interface. Call <strong>QueryInterface</strong> to obtain a pointer to the [IPrintPipelineProgressReport](https://msdn.microsoft.com/library/windows/hardware/ff554314) interface.</p></td>
</tr>
<tr class="odd">
<td><p>PrinterHandle</p></td>
<td><p>XPS_FP_PRINTER_HANDLE</p></td>
<td><p>VT_BYREF</p></td>
<td><p>The printer handle. The filter should not close this handle.</p></td>
</tr>
<tr class="even">
<td><p>PerUserPrintTicket</p></td>
<td><p>XPS_FP_USER_PRINT_TICKET</p></td>
<td><p>VT_UNKNOWN</p></td>
<td><p>A pointer to an <strong>IUnknown</strong> interface. Call <strong>QueryInterface</strong> to obtain a pointer to the [IPrintReadStreamFactory](https://msdn.microsoft.com/library/windows/hardware/ff554338) interface.</p></td>
</tr>
<tr class="odd">
<td><p>UserSecurityToken</p></td>
<td><p>XPS_FP_USER_TOKEN</p></td>
<td><p>VT_BYREF</p></td>
<td><p>A handle that the filter can use to impersonate the user account that submitted the print job.</p></td>
</tr>
<tr class="even">
<td><p>PrintJobId</p></td>
<td><p>XPS_FP_JOB_ID</p></td>
<td><p>VT_UI4</p></td>
<td><p>The print job identification number.</p></td>
</tr>
<tr class="odd">
<td><p>PrintClassFactory</p></td>
<td><p>XPS_FP_PRINT_CLASS_FACTORY</p></td>
<td><p>VT_UNKNOWN</p></td>
<td><p>A pointer to an <strong>IUnknown</strong> interface. Call <strong>QueryInterface</strong> to obtain a pointer to the [IPrintClassObjectFactory](https://msdn.microsoft.com/library/windows/hardware/ff551955) interface.</p></td>
</tr>
<tr class="even">
<td><p>IPrintCoreHelper</p></td>
<td><p>(There is no symbolic name for this property name.)</p></td>
<td><p>VT_UNKNOWN</p></td>
<td><p>A pointer to an <strong>IUnknown</strong> interface. Call <strong>QueryInterface</strong> to obtain a pointer to the [IPrintCoreHelper](https://msdn.microsoft.com/library/windows/hardware/ff552960) interface.</p>
<p>Note that this property is only available in XPSDrv printer drivers that use the unidrvui.dll as the configuration UI DLL.</p></td>
</tr>
<tr class="odd">
<td><p>PrintDeviceCapabilities</p></td>
<td><p>XPS_FP_PRINTDEVICECAPABILITIES</p></td>
<td><p>VT_UNKNOWN</p></td>
<td><p>A pointer to an <strong>IUnknown</strong> interface. Call <strong>QueryInterface</strong> to obtain a pointer to the [IPrintReadStreamFactory](https://msdn.microsoft.com/library/windows/hardware/ff554338) interface.</p>
<p>Allows XPS rendering filters to retrieve PrintDeviceCapabilities XML files from the Print filter pipeline property bag.</p></td>
</tr>
</tbody>
</table>

 

## <span id="see_also"></span>See also


[V4 Printer Driver Property Bags](https://msdn.microsoft.com/library/windows/hardware/jj218738)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Print%20Pipeline%20Property%20Bag%20%20RELEASE:%20%281/8/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





