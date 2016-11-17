---
title: Unidrv/PScript5 Plug-in Configuration Modules
author: windows-driver-content
description: Unidrv/PScript5 Plug-in Configuration Modules
MS-HAID:
- 'xpsconfig\_5e4511e1-2318-4290-ad7f-75a690422448.xml'
- 'print.unidrv\_pscript5\_plug\_in\_configuration\_modules'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 806175ba-18a9-48f3-8f50-06e794d1f304
keywords: ["Version 3 XPS drivers WDK XPSDrv , Unidrv plug-in", "Version 3 XPS drivers WDK XPSDrv , PScript5 plug-in", "IPrintCoreHelper", "Pscript WDK print , XPSDrv print drivers", "Unidrv, XPSDrv print drivers", "Unidrv WDK print"]
---

# Unidrv/PScript5 Plug-in Configuration Modules


XPSDrv print driver configuration modules that use Unidrv or PScript5 configuration plug-ins in Windows Vista support the following new features:

-   The PrintTicket and PrintCapabilities features

-   The [IPrintCoreHelper](https://msdn.microsoft.com/library/windows/hardware/ff552960) interface for manipulating Unidrv and PScript5 settings

-   XPSDrv Document events

-   Communication with print driver filters in the filter pipeline

### PrintTicket and PrintCapabilities Interface Support

Unidrv and PScript5 print driver plug-ins implement the [IPrintOemPrintTicketProvider](https://msdn.microsoft.com/library/windows/hardware/ff553174) interface to customize the PrintTicket and PrintCapabilities data. The methods in this interface allow a plug-in to customize PrintTicket and PrintCapabilities processing for the custom features that the plug-in provides.

The Unidrv and PScript5 print drivers implement the [IPrintTicketProvider](https://msdn.microsoft.com/library/windows/hardware/ff554375) interface and generate the initial version of the PrintTicket and PrintCapabilities data that is based on the GPD or PPD file. After the initial processing, the Unidrv or PScript5 print driver then calls the plug-in's **IPrintOemPrintTicketProvider** interface so that the plug-in can modify this data before the print driver returns it to the calling application.

### IPrintCoreHelper Interface

The **IPrintCoreHelper** interface enables the print driver configuration plug-in to:

-   Get and set values in the private portion of the DEVMODE structure that Unidrv and PScript5 print drivers use.

-   Enumerate print driver features, options, and constraints.

-   Access the complete GPD or partial PPD file content.

The only way for a plug-in to properly set the Unidrv or PScript5 configuration and enable full user interface (UI) replacement functionality is by using the following **IPrintCoreHelper** interface.

```
DECLARE_INTERFACE_(IPrintCoreHelper, IUnknown) {
  // IUnknown methods skipped
  STDMETHOD(CreateInstanceOfMSXMLObject)(...)
  STDMETHOD(EnumConstrainedOptions)(...)
  STDMETHOD(EnumFeatures)(...)
  STDMETHOD(EnumOptions)(...)
  STDMETHOD(GetOption)(...)
  STDMETHOD(SetOptions)(...)
  STDMETHOD(WhyConstrained)(...)
};
```

The following two additional interfaces, [IPrintCoreHelperUni](https://msdn.microsoft.com/library/windows/hardware/ff552940) and [IPrintCoreHelperPS](https://msdn.microsoft.com/library/windows/hardware/ff552906), are derived from the **IPrintCoreHelper** interface. These interfaces are specific to Unidrv and PScript5 print drivers, respectively, and include additional methods that are unique to each driver.

```
DECLARE_INTERFACE_(IPrintCoreHelperUni, IUnknown) {
  // IUnknown methods skipped
  // IPrintCoreHelper methods skipped
  STDMETHOD(CreateDefaultGDLSnapshot)(...)
  STDMETHOD(CreateGDLSnapshot)(...)
};

DECLARE_INTERFACE_(IPrintCoreHelperPS, IUnknown) {
  // IUnknown methods skipped
  // IPrintCoreHelper methods skipped
  STDMETHOD(GetFeatureAttribute)(...)
  STDMETHOD(GetGlobalAttribute)(...)
  STDMETHOD(GetOptionAttribute)(...)
};
```

The following code example illustrates how you can use the **IPrintCoreHelper** interface to query information from the DEVMODE structure. This example is part of the XPSDrv print driver sample code in the Windows Driver Kit (WDK).

```
HRESULT
CBookletDMPTConv::GetDrvSettingsFromDM(
    __in    PDEVMODE                         pDevmode,
            ULONG                            cbDevmode,
    __out   GPD::Binding::DrvSettings*       pDrvSettings
    )
{
  HRESULT hr = S_OK;

  for (GPD::Binding::EGPDSettings setting = 
        GPD::Binding::EGPDSettingsMin;
      setting < GPD::Binding::EGPDSettingsMax && SUCCEEDED(hr);
      setting++)
  {
    PCSTR pszOption;
    hr = m_pCoreHelper->GetOption(
      pDevmode,
      cbDevmode, 
      m_featureNames[setting], 
      &pszOption)
    if (SUCCEEDED(hr))
    {
      hr = GPDSettingFromOptionString(
      pszOption, 
      setting, 
      pDrvSettings);
    }
  }

  return hr;
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Unidrv/PScript5%20Plug-in%20Configuration%20Modules%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


