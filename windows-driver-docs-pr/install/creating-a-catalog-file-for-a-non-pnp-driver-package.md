---
title: Creating a Catalog File for a Non-PnP Driver Package
description: Creating a Catalog File for a Non-PnP Driver Package
ms.assetid: b40a6f42-53a8-468f-abf1-335c5ead3cbd
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a Catalog File for a Non-PnP Driver Package


You can use the [MakeCat](http://go.microsoft.com/fwlink/p/?linkid=104922) tool to create a [catalog file](catalog-files.md) for a non-PnP [driver package](driver-packages.md).

**Note**  You must use the MakeCat tool only to create catalog files for driver packages that are not installed by using an INF file. If the driver package is installed by using an INF file, use the [**Inf2Cat**](https://msdn.microsoft.com/library/windows/hardware/ff547089) tool to create the catalog file. Inf2Cat automatically includes all the files in the driver package that are referenced within the package's INF file. For more information about how to use the Inf2Cat tool, see [Using Inf2Cat to Create a Catalog File](using-inf2cat-to-create-a-catalog-file.md).

 

To create a catalog file, you must first manually create a Catalog Definition File (.*.cdf*) that describes the catalog header attributes and file entries. After this file is created, you can then run the [MakeCat](http://go.microsoft.com/fwlink/p/?linkid=104922) tool to create a catalog file

### Creating a catalog file

To create a catalog file for a non-PnP driver package, follow these steps:

1.  Use a text editor to create a .*.cdf* file that lists the name of the [catalog file](catalog-files.md) to be created, its attributes, and the names of the files that are to be listed in the catalog file.

2.  Use the [MakeCat](http://go.microsoft.com/fwlink/p/?linkid=104922) command-line tool to create the catalog file. For more information about the MakeCat tool, see the [Using MakeCat](http://go.microsoft.com/fwlink/p/?linkid=70086) website.

3.  Install the catalog file on a computer on which the driver will be installed.

### Overview of the MakeCat tool

The MakeCat tool does the following when it processes the .*.cdf* file:

-   Verifies the attributes of the [catalog file](catalog-files.md) that is defined by the .*.cdf* file, and adds the attributes to the catalog file.

-   Verifies the attributes for each file that is listed within the .*.cdf* file, and adds the attributes to the catalog file.

-   Generates a cryptographic hash, or *thumbprint*, of each of the listed files.

-   Stores each file's thumbprint in the catalog file.

Use the following MakeCat command to create a catalog file.

```cpp
MakeCat -v CatalogDefinitionFileName..cdf
```

Where:

-   The **-v** option configures MakeCat to print execution and warning messages.

-   *CatalogDefinitionFileName..cdf* is the name of the catalog definition file.

### Examples

The following example shows the contents of a typical catalog definition file that is named Good..cdf. The package to be cataloged contains two files, *File1* and *File2*. The resulting catalog file is named Good.cat.

```cpp
[CatalogHeader]
Name=Good.cat
PublicVersion=0x0000001
EncodingType=0x00010001
CATATTR1=0x10010001:OSAttr:2:6.0
[CatalogFiles]
<hash>File1=File1
<hash>File2=File2
```

The options that are used in this example are described below. For more information about these options, see the [MakeCat](http://go.microsoft.com/fwlink/p/?linkid=104922) website.

<a href="" id="name-good-cat"></a>Name=Good.cat  
Specifies the name of the catalog file (*Good.cat*).

<a href="" id="publicversion-0x0000001"></a>PublicVersion=0x0000001  
Specifies the version of the catalog file.

<a href="" id="encodingtype-0x00010001"></a>EncodingType=0x00010001  
Specifies the message encoding type that is used to generate the thumbprint. The value 0x00010001 specifies a message encoding type of PKCS_7_ASN_ENCODING | X509_ASN_ENCODING.

<a href="" id="catattr1-0x10010001-osattr-2-6-0"></a>CATATTR1=0x10010001:OSAttr:2:6.0  
Specifies an attribute of the catalog file. To specify additional attributes, you must use separate CATATTR options, with each option assigned a unique numeric digit as a suffix. For example, use CATATT1 to specify one catalog file attribute and CATATT2 to specify another.

In this example, the attribute specified by using the CATATTR1 option has the following value:

<a href="" id="0x10010001"></a>0x10010001  
Specifies the attribute to be the following:

-   0x10000000 - Authenticated attribute (signed, included in the thumbprint).

-   0x00010000 - Attribute is represented in plain text.

-   0x00000001 - Attribute is a name-value pair.

<a href="" id="osattr-2-6-0"></a>OSAttr:2:6.0  
The OSAttr attribute specifies the target Windows version whose signing requirements are compatible with the [driver package](driver-packages.md). The attribute's value specifies the following:

-   The value *2* specifies the catalog file is compatible with NT-based versions of the Windows operating system.

-   The value *6.0* specifies the catalog file is compatible with Windows Vista.
    **Note**  If the [driver package](driver-packages.md) is compatible with multiple Windows versions, you must use separate CATATTR options to specify the OSAttr attribute for each Windows version.

     

<a href="" id="-hash-file1-file1"></a>&lt;hash&gt;File1=File1  
Specifies a reference tag for the file File1 which is referenced through the catalog file. The value *&lt;hash&gt;File1* results in the tag being the file's cryptographic hash, or *thumbprint*.

<a href="" id="-hash-file1-file2"></a>&lt;hash&gt;File1=File2  
Specifies a reference tag for the file, File2, which is referenced through the catalog file. The value *&lt;hash&gt;File2* results in the tag being the file's thumbprint.

The following example shows how to generate the [catalog file](catalog-files.md), *Good.cat,* from a corresponding catalog definition file *Good..cdf*. Makecat saves *Good.cat* in the same folder where *File1* and *File2* are located.

```cpp
MakeCat -v Good.cdf
```

 

 





