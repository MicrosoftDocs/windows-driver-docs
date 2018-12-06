---
title: Filter Pipeline Configuration File
description: Filter Pipeline Configuration File
ms.assetid: 586247bd-6d06-4728-a5f0-ee3fe1d09321
keywords:
- XPSDrv printer drivers WDK , render modules
- render modules WDK XPSDrv , filter pipeline configuration files
- filter pipeline configuration files WDK XPSDrv
- private keywords WDK XPSDrv
- filter pipeline property bags WDK XPSDrv
- property bags WDK filter pipeline
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter Pipeline Configuration File


The *filter pipeline configuration file* is an XML file that defines the following:

-   Order of the filters in the pipeline. This order is defined by the ordering of the XML elements in the filter pipeline configuration file.

-   Filter interfaces. These interfaces are defined by XML attributes in the filter pipeline configuration file.

-   Input and output formats for each filter. These formats are defined by XML elements in the filter pipeline configuration file.

The following code example shows a typical filter pipeline configuration file:

```xml
<Filters>
    <Filter      dll="XDWMark.dll"
 clsid="{D647D658-BEF6-415f-AFAC-070D64074C5D}"
                name="Watermark filter">
        <Input  guid="{b8cf8530-5562-47c4-ab67-b1f69ecf961e}" comment="IID_IXpsDocumentProvider"/>
        <Output guid="{4368d8a2-4181-4a9f-b295-3d9a38bb9ba0}" comment="IID_IXpsDocumentConsumer"/>
    </Filter>
 <Filter dll="XDScale.dll"
 clsid="{B9B52406-92D3-4721-86E6-3CF78F6D5FC5}"
 name="Page Scaling filter">
 <Input guid="{4d47a67c-66cc-4430-850e-daf466fe5bc4}" comment="IID_IPrintReadStream"/>
 <Output guid="{65bb7f1b-371e-4571-8ac7-912f510c1a38}" comment="IID_IPrintWriteStream"/>
 </Filter>
    <Filter      dll="XDColMan.dll"
 clsid="{8E56FC37-0799-447e-A643-16F4FB18244C}"
 name="Colour Management filter">
         <Input guid="{b8cf8530-5562-47c4-ab67-b1f69ecf961e}" comment="IID_IXpsDocumentProvider"/>
        <Output guid="{4368d8a2-4181-4a9f-b295-3d9a38bb9ba0}" comment="IID_IXpsDocumentConsumer"/>
    </Filter>
    <Filter      dll="XDBook.dll"
 clsid="{7DFC96C6-CEA2-46d8-B354-887C47B7986D}"
                name="Booklet filter">
         <Input guid="{b8cf8530-5562-47c4-ab67-b1f69ecf961e}" comment="IID_IXpsDocumentProvider"/>
        <Output guid="{4368d8a2-4181-4a9f-b295-3d9a38bb9ba0}" comment="IID_IXpsDocumentConsumer"/>
    </Filter>
    <Filter      dll="XDNUp.dll"
 clsid="{1b5bee16-511c-440f-8017-2123f481091a}"
                name="NUp filter">
         <Input guid="{b8cf8530-5562-47c4-ab67-b1f69ecf961e}" comment="IID_IXpsDocumentProvider"/>
        <Output guid="{4368d8a2-4181-4a9f-b295-3d9a38bb9ba0}" comment="IID_IXpsDocumentConsumer"/>
    </Filter>
</Filters>
```

### Private Keywords

An [XPSDrv configuration module](xpsdrv-configuration-module.md) can put *private keywords* in the PrintTicket entry when it handles an [XPS driver document event](xps-driver-document-events.md) during a [**DrvDocumentEvent**](https://msdn.microsoft.com/library/windows/hardware/ff548544) function call. These PrintTicket entries are then read by the processing filters in the print filter pipeline while the filters are reading the PrintTicket.

### Filter Pipeline Property Bag

A configuration module can also use the *filter pipeline property bag* to store data or to pass information to a filter pipeline. To expose configuration services by using the property bag, the configuration module must export the **DrvPopulateFilterServices** method. In addition, the filter pipeline configuration file must include the **&lt;FilterServiceProvider&gt;** element for each service. The provider module must implement and export the **DllCanUnloadNow** function. Typically, these providers publish COM interfaces in the property bag. The provider must stay loaded while these interfaces are in use.

Another element, **&lt;OptionalFilterServiceProvider&gt;**, allows the pipeline manager to continue the print job if the service provider dll is not available. The individual filters must define their behavior in the absence of the optional service provider. Otherwise, if **&lt;FilterServiceProvider&gt;** is used and the dll cannot be loaded, the job fails. The **&lt;OptionalFilterServiceProvider&gt;** element is supported in Windows 7 and later.

The following code example shows the **DrvPopulateFilterServices** function:

```cpp
HRESULT
DrvPopulateFilterServices(
    __in IPrintPipelinePropertyBag  *pPropertyBag
    );
```

For more information about preceding function, see [**DrvPopulateFilterServices**](https://msdn.microsoft.com/library/windows/hardware/hh768268).

The following code example shows the XML syntax for the **&lt;FilterServiceProvider&gt;** element in the filter pipeline configuration file:

```xml
<Filters>
    <Filter ... />
    <FilterServiceProvider dll = "providerA.dll"/>
    <FilterServiceProvider dll = "providerB.dll"/>
</Filters>
```

### Interleaving Mode for the Output Device

*Interleaving* refers to how the individual resource parts of an XPS document are streamed along with the FixedPage document parts. When the filter pipeline creates the XPS document object model for the first filter with XPS document interfaces in the pipeline, the interleaving order of the XPS spool file is no longer followed. However, the last filter in the pipeline that uses the XPS document interface can specify an interleaving order in the filter configuration file for the pipeline to use when it serializes the XPS content. Selecting the interleaving order that is most compatible with an output device or an output file can improve the performance of subsequent document processing.

The following example filter is an excerpt from the preceding example filter configuration file that has been modified to show how to use the interleaving option. Although this example shows both interleaving options for the purpose of illustration, a real filter configuration file has only one **&lt;Interleaving&gt;** element in the filter definition:

```xml
    <Filter     dll="XDNUp.dll"
      clsid="{1b5bee16-511c-440f-8017-2123f481091a}"
        name="NUp filter">
      <Input guid="{b8cf8530-5562-47c4-ab67-b1f69ecf961e}" comment="IID_IXpsDocumentProvider"/>
       <Output guid="{4368d8a2-4181-4a9f-b295-3d9a38bb9ba0}" comment="IID_IXpsDocumentConsumer"/>
     <Interleaving mode="ResourcesFirst"\>
     <Interleaving mode="MarkupFirst"\>
    </Filter>
```

The filter pipeline supports the following interleaving orders:

-   The **ResourcesFirst** interleaving order streams each dependent resource before the FixedPage that depends on the resource. This interleaving order is good for printer drivers and for direct-consumption printers because it provides the font and image resources that the printer requires to render the text and page content just before the rendering begins.

-   The **MarkupFirst** interleaving order streams the document text and markup and the information about how a resource will be used before it streams the actual resource. This interleaving order is best for archive file destinations and for applications that view the document online.

### Archive-Optimized XPS Output

This feature allows print drivers to explicitly request archive-optimized XPS output as a spool file. In Windows 8, the Microsoft XPS Document Writer v4 (MXDW) produces this archive-ready XPS output via a code path that is only available to MXDW in the Microsoft XPS Document Converter (MXDC). So a print driver can generate this archive-optimized XPS from MXDC.

The following code example shows the XML syntax for using the &lt;Archive&gt; element in the filter pipeline configuration file to enable this feature:

```xml
<Filters>
    ...
    <Archive enabled="true"/>
</Filters>
```
