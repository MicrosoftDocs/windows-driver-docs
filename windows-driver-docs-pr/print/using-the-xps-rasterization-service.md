---
title: Use the XPS Rasterization Service
description: Provides information about how to use the XPS rasterization service.
ms.date: 01/31/2023
---

# Use the XPS rasterization service

[!include[Print Support Apps](../includes/print-support-apps.md)]

The XPS rasterization service implements XPS rasterizer objects that convert fixed pages in XPS documents to bitmaps. This service simplifies the design of an XPSDrv filter that renders an XPS document as a series of bitmap images. The filter can tell an XPS rasterizer object to create a bitmap image of an axis-aligned, rectangular region in a fixed page.

For example, an XPSDrv filter for a printer might require a fixed page to be sent to the printer as a series of horizontal or vertical bands. In this case, the filter tells the XPS rasterizer object to rasterize each band as a separate bitmap. Alternatively, if the printer has sufficient memory, the filter might tell the rasterizer to create a bitmap image of the entire page.

The XPS rasterization service is implemented in the system file Xpsrasterservice.dll. However, XPSDrv filters do not directly access the entry points in this DLL. Instead, a filter accesses the interfaces of the XPS rasterization service through the [**print pipeline property bag**](./print-pipeline-property-bag.md) that the filter receives from the print filter pipeline manager.

To be available for use by an XPSDrv filter, the XPS rasterization service must be specified in the [filter pipeline configuration file](filter-pipeline-configuration-file.md) that describes the filters in the print filter pipeline. Specifically, the configuration file must contain a **FilterServiceProvider** element with a **dll** attribute set to the service DLL name, as shown in the following XML example:

```xml
<FilterServiceProvider dll = "XpsRasterService.dll" />
```

The **FilterServiceProvider** element is a child of the **Filters** element that lists the filters in the pipeline. During pipeline initialization, the print filter pipeline manager loads the XPS rasterization service and makes the service accessible to the filter through the property bag. For an example of a filter pipeline configuration file that loads the XPS rasterization service, see the XpsRasFilter sample in the WDK. This sample is located in the Src\\Print\\Xpsrasfilter folder in your WDK installation.

## Obtaining an XPS rasterization factory

Before rasterizing an XPS document, an XPSDrv filter must retrieve a reference to the rasterization factory object from the print pipeline property bag. Thereafter, the filter obtains a new XPS rasterizer object from the factory for each fixed page that it needs to render.

To initialize an XPSDrv filter, the print filter pipeline manager calls the filter's [**IPrintPipelineFilter::InitializeFilter**](/windows-hardware/drivers/ddi/filterpipeline/nf-filterpipeline-iprintpipelinefilter-initializefilter) method and passes the property bag's [IPrintPipelinePropertyBag](/windows-hardware/drivers/ddi/filterpipeline/nn-filterpipeline-iprintpipelinepropertybag) interface to the method as an input parameter.

To obtain a pointer to the XPS rasterization factory object, the XPSDrv filter calls the [**IPrintPipelinePropertyBag::GetProperty**](/windows-hardware/drivers/ddi/filterpipeline/nf-filterpipeline-iprintpipelinepropertybag-getproperty) method. The property name "MS_IXpsRasterizationFactory" identifies the rasterization factory object. For this property, the value obtained from **GetProperty** is a reference to the rasterization factory object's **IUnknown** interface. After obtaining this interface, the filter must call the [IUnknown::QueryInterface](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) method to obtain a reference to the object's [IXpsRasterizationFactory](/windows-hardware/drivers/ddi/xpsrassvc/nn-xpsrassvc-ixpsrasterizationfactory) interface. Subsequently, the filter can call the [**IXpsRasterizationFactory::CreateRasterizer**](/windows-hardware/drivers/ddi/xpsrassvc/nf-xpsrassvc-ixpsrasterizationfactory-createrasterizer) method to create XPS rasterizer objects.

When the factory object is no longer needed, the filter should release the object by calling the [Release](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) method on the object's **IXpsRasterizationFactory** interface.

The following code example shows how to obtain an **IXpsRasterizationFactory** interface instance from an **IPrintPipelinePropertyBag** interface instance:

```cpp
//
// Retrieve a reference to the XPS rasterization factory
// from the print pipeline property bag.
//
HRESULT CreateRasterizationFactory(
 IPrintPipelinePropertyBag *pPropertyBag,
 IXpsRasterizationFactory **ppXPSRasFactory)
{
    if (ppXPSRasFactory != NULL)
    {
        *ppXPSRasFactory = NULL;
    }

    if (pPropertyBag == NULL || ppXPSRasFactory == NULL)
    {
        return E_POINTER;
    }

    HRESULT hr;
    VARIANT var;
 IXpsRasterizationFactory *pXPSRasFactory;

    //
    // Retrieve the factory object from the property bag.
    //
 VariantInit(&var);
    hr = pPropertyBag->GetProperty(L"MS_IXpsRasterizationFactory",
                                   &var);
    if (SUCCEEDED(hr))
    {
        assert(var.vt == VT_UNKNOWN && var.punkVal != NULL);

        //
        // Get the factory object's IXpsRasterizationFactory interface.
        //
 IUnknown *pUnknown = var.punkVal;

        hr = pUnknown->QueryInterface(__uuidof(IXpsRasterizationFactory),
 reinterpret_cast<void**>(&pXPSRasFactory));
    }

    if (SUCCEEDED(hr))
    {
        //
        // Give the caller our reference to the IXpsRasterizationFactory interface.
        //
        *ppXPSRasFactory = pXPSRasFactory;
    }

 VariantClear(&var);
    return hr;
}
```

## Creating an XPS object model of a fixed page

After creating an XPS rasterization factory, an XPSDrv filter can use the factory to create XPS rasterizer objects. An XPS rasterizer object has an [IXpsRasterizer](/windows-hardware/drivers/ddi/xpsrassvc/nn-xpsrassvc-ixpsrasterizer) interface. Each XPS rasterizer object is dedicated to a particular fixed page of an XPS document. To create an XPS rasterizer object, a factory requires an XPS object model (OM) of the fixed page. The XPS OM (of the fixed page) is contained in an object that has an **IXpsOMPage** interface. The XPS rasterizer object uses this interface to access the contents of the fixed page. For more information about the **IXpsOMPage** interface, see the Windows SDK documentation.

The XPSDrv filter follows these steps to create an XPS rasterizer object:

- The filter reads a fixed page object with an [IFixedPage](/windows-hardware/drivers/ddi/filterpipeline/nn-filterpipeline-ifixedpage) interface from the input stream.

- The filter creates an XPS OM object with an **IXpsOMPage** interface to hold the contents of the fixed page. The XPS rasterizer will later use this interface to access the contents of the fixed page.

- To create the XPS rasterizer object, the filter passes the XPS OM object's **IXpsOMPage** interface to the XPS rasterization factory's **IXpsRasterizationFactory::CreateRasterizer** method.

When the XPS rasterizer object is no longer needed, the filter should release the object by calling the **Release** method on the object's **IXpsRasterizer** interface. For an example implementation of an XPSDrv filter that uses the XPS rasterization service, see the XpsRasFilter sample driver in the WDK.

For use with XPS Rasterization Service, canvases and visual brushes within a fixed page can be nested up to a limit of 64 levels. For more information about canvases and visual brushes, download the [XML Paper Specification](https://download.microsoft.com/download/1/6/a/16acc601-1b7a-42ad-8d4e-4f0aa156ec3e/xps_1_0.zip).

## Bitmap resolution and pixel format

The XPS rasterizer object for a fixed page must know the resolution at which the page will be rendered. The XPSDrv filter specifies this resolution, in dots per inch (DPI), as an input parameter in the call to **IXpsRasterizationFactory::CreateRasterizer** that creates the XPS rasterizer object. For example, if a display device has a resolution of 600 DPI, and a fixed page describes a standard letter-size page, a bitmap image of the entire page has the following dimensions:

width = (8.5 inches)x(600 DPI) = 5100 dots

height = (11 inches)x(600 DPI) = 6600 dots

To create a bitmap image of rectangular region of a fixed page, an XPSDrv filter calls the XPS rasterizer object's [**IXpsRasterizer::RasterizeRect**](/windows-hardware/drivers/ddi/xpsrassvc/nf-xpsrassvc-ixpsrasterizer-rasterizerect) method. This method always produces a bitmap with a pixel size of 32 bits. The pixel format is specified by the GUID value **GUID_WICPixelFormat32bppPBGRA**, which is defined in header file Wincodec.h. The format contains 8-bit red, green, and blue components and uses the standard (sRGB) color space. In addition, the format contains an 8-bit alpha component. The color components in each pixel value are premultiplied by the alpha component. For more information about this format, see [Native Pixel Formats Overview](/windows/desktop/wic/-wic-codec-native-pixel-formats).

Some XPSDrv filters might perform additional processing of a bitmap produced by an XPS rasterizer object. For example, a filter for a color printer might convert the bitmap to a CMYK pixel format before wrapping the bitmap in the printer's page description language and sending it to the printer.

For more information about the interfaces that the XPS rasterization service uses to communicate with XPSDrv filters, see the [xpsrassvc.h](/windows-hardware/drivers/ddi/_print/index) header DDI reference.

## XPSRas and high precision pixel formats

- In Windows 8, the XPS rasterization service exposes a new interface, [IXpsRasterizationFactory1](/windows-hardware/drivers/ddi/xpsrassvc/nn-xpsrassvc-ixpsrasterizationfactory1), which is a new version of [IXpsRasterizationFactory](/windows-hardware/drivers/ddi/xpsrassvc/nn-xpsrassvc-ixpsrasterizationfactory). **IXpsRasterizationFactory1** exposes a new method, [**IXpsRasterizationFactory1::CreateRasterizer**](/windows-hardware/drivers/ddi/xpsrassvc/nf-xpsrassvc-ixpsrasterizationfactory1-createrasterizer), that is identical to the Windows 7 version ([**IXpsRasterizationFactory::CreateRasterizer**](/windows-hardware/drivers/ddi/xpsrassvc/nf-xpsrassvc-ixpsrasterizationfactory-createrasterizer)), except that it takes one new parameter for output pixel format.

- This feature exposes a new enumeration, [**XPSRAS_PIXEL_FORMAT**](/windows-hardware/drivers/ddi/xpsrassvc/ne-xpsrassvc-__midl___midl_itf_xpsrassvc_0000_0003_0001), that allows a caller to select the pixel format used by the [IWICBitmap](/windows/win32/api/wincodec/nn-wincodec-iwicbitmap) interface that is returned by the IXpsRasterizer::RasterizeRect method.

## XPSRas and the GPU

If you have a computer that is running Windows 8 with a WDDM 1.2 display driver, and all the conditions shown in the [XPSRas GPU Usage Decision Tree](xpsras-usage-decision-tree.md) have been met, then GPU hardware acceleration is always used. This means that, as a developer, you do not have to perform any steps to benefit from the performance enhancements provided by the GPU. However, to further optimize the graphics performance of your system, you should consider doing the following:

- Call the [**RasterizeRect**](/windows-hardware/drivers/ddi/xpsrassvc/nf-xpsrassvc-ixpsrasterizer-rasterizerect) method with consistent rectangle dimensions. If this is not possible, it is optimal to provide **RasterizeRect** with the largest required rectangle size on the first invocation, and ask for smaller rectangle sizes on subsequent calls.

- Use anti-aliasing only when it is absolutely required. Aliased text and vectors look the same as their anti-aliased counterparts, when the DPI value provided to the [**IXpsRasterizationFactory::CreateRasterizer**](/windows-hardware/drivers/ddi/xpsrassvc/nf-xpsrassvc-ixpsrasterizationfactory-createrasterizer) method is considerably high. For example, a DPI value greater than 200DPI is considered to be high. Testing should be done to ensure that output quality on a given device is sufficient when using aliased text and vectors along with a high DPI.

- If a document can be manipulated prior to rasterizing the IXpsOMPage, then subsetting fonts and using resource dictionaries for elements repeated on several pages will improve XPSRas performance.
