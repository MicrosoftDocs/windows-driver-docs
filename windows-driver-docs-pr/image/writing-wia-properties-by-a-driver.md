---
title: Writing WIA Properties by a Driver
description: Writing WIA Properties by a Driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing WIA Properties by a Driver





A WIA minidriver can update any of the current values of its WIA properties and valid values by using the following WIA service functions:

<a href="" id="wiaswritemultiple"></a>[**wiasWriteMultiple**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritemultiple)  
Write all WIA property types. This is a general function that allows a WIA driver to write any property existing on a WIA item, including custom properties. It can be used to write to multiple properties per call.

<a href="" id="wiaswritepropstr"></a>[**wiasWritePropStr**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritepropstr)  
Write WIA properties that are strings (type VT\_BSTR).

<a href="" id="wiaswriteproplong"></a>[**wiasWritePropLong**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswriteproplong)  
Write WIA properties that are four-byte integers (type VT\_I4).

<a href="" id="wiaswritepropfloat"></a>[**wiasWritePropFloat**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritepropfloat)  
Write WIA properties that are four-byte real numbers (type VT\_R4).

<a href="" id="wiaswritepropguid"></a>[**wiasWritePropGuid**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritepropguid)  
Write WIA properties that are GUIDs (type VT\_CLSID).

<a href="" id="wiaswritepropbin"></a>[**wiasWritePropBin**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritepropbin)  
Write WIA properties that are strings of unsigned bytes (type VT\_VECTOR | VT\_UI1).

<a href="" id="wiasgetchangedvaluelong"></a>[**wiasGetChangedValueLong**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchangedvaluelong)  
Get the current changed information for WIA properties that are four-byte integers (type VT\_I4).

<a href="" id="wiasgetchangedvaluefloat"></a>[**wiasGetChangedValueFloat**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchangedvaluefloat)  
Get the current changed information for WIA properties that are four-byte real numbers (type VT\_R4).

<a href="" id="wiasgetchangedvalueguid"></a>[**wiasGetChangedValueGuid**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchangedvalueguid)  
Get the current changed information for WIA properties that are GUIDs (type VT\_CLSID).

<a href="" id="wiasgetchangedvaluestr"></a>[**wiasGetChangedValueStr**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchangedvaluestr)  
Get the current changed information for WIA properties that are strings (type VT\_BSTR).

<a href="" id="wiascreatepropcontext"></a>[**wiasCreatePropContext**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreatepropcontext)  
Create a WIA property context, which is used in the [**wiasGetChangedValueLong**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchangedvaluelong), [**wiasGetChangedValueFloat**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchangedvaluefloat), [**wiasGetChangedValueGuid**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchangedvalueguid), and [**wiasGetChangedValueStr**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchangedvaluestr) service functions.

<a href="" id="wiasfreepropcontext"></a>[**wiasFreePropContext**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasfreepropcontext)  
Free the allocated context memory that was created by [**wiasCreatePropContext**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreatepropcontext).

### <a href="" id="implementing-iwiaminidrv-drvvalidateitemproperties"></a>Implementing IWiaMiniDrv::drvValidateItemProperties

The [**IWiaMiniDrv::drvValidateItemProperties**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvvalidateitemproperties) method is called when changes are made to an item's WIA properties. The WIA minidriver should not only check that the values are valid, but must update any valid values that change.

If a WIA property is invalid, andthe application is not writing to it, the invalid value and any dependent values must be changed to valid values, or else fail validation (because the application is setting the property to an invalid value).

The following example shows an implementation of the **IWiaMiniDrv::drvValidateItemProperties** method:

```cpp
HRESULT _stdcall CWIADevice::drvValidateItemProperties(
  BYTE           *pWiasContext,
  LONG           lFlags,
  ULONG          nPropSpec,
  const PROPSPEC *pPropSpec,
  LONG           *plDevErrVal)
{
  //
  // If the caller did not pass in the correct parameters,
  //  then fail the call with E_INVALIDARG.
  //

  if (!pWiasContext) {
      return E_INVALIDARG;
  }

  if (!plDevErrVal) {
      return E_INVALIDARG;
  }

  if (!pPropSpec) {
      return E_INVALIDARG;
  }

  HRESULT hr      = S_OK;
  LONG lItemType  = 0;
  WIA_PROPERTY_CONTEXT Context;

  *plDevErrVal = 0;

  //
  // create a WIA property context, to gain access to
  // the WIA application's intended settings.
  //

  hr = wiasCreatePropContext(nPropSpec,
                             (PROPSPEC*)pPropSpec,
                             0,
                             NULL,
                             &Context);
  if(S_OK == hr) {

    //
    // get the current item type to help determine what property set to validate
    //

      hr = wiasGetItemType(pWiasContext, &lItemType);
      if (S_OK == hr) {
          if (lItemType & WiaItemTypeRoot) {

            //
            //  validate root item properties here
            //

        } else {

            //
            // validate item properties here
            //

              WIAS_CHANGED_VALUE_INFO cviDataType;
              memset(&cviDataType,0,sizeof(cviDataType));

            //
            // check to see if the application was updating
            // the WIA_IPA_DATATYPE property
   //

              hr = wiasGetChangedValueLong(pWiasContext,pContext,FALSE,WIA_IPA_DATATYPE,&cviDataType);
              if(S_OK == hr) {
                  if (cviDataType.bChanged) {

                    //
                    // This value was changed, and needs to be checked
                    //
                    // cviDataType.Current.lVal is the current application setting.
                    //

                  } else {

                    //
                    // Nothing has been changed, so leave this property alone.
                    // Let the WIA service function wiasValidateItemProperties
                    // do the rest of the work for you.
                    //

 }
              }
          }

        //
        // free the property context
        //

          wiasFreePropContext(&Context);
      }

    //
    // call WIA service helper when you have finished updating dependent values
    //

    if(S_OK == hr) {

        //
        // call WIA service helper to validate other properties
        //

          hr = wiasValidateItemProperties(pWiasContext, nPropSpec, pPropSpec);
      }
  }
  return hr;
}
```

 

