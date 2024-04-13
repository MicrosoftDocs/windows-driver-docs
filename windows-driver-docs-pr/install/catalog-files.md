---
title: Catalog Files and Digital Signatures
description: Catalog Files and Digital Signatures
keywords:
- thumbprints WDK driver signing
- signed catalog files WDK driver signing
- .cat files
- CAT files
- driver signing WDK , catalog files
- signing drivers WDK , catalog files
- digital signatures WDK , catalog files
- signatures WDK , catalog files
- catalog files WDK driver signing
ms.date: 04/20/2017
---

# Catalog Files and Digital Signatures

A digitally-signed catalog file (*.cat*) can be used as a digital signature for an arbitrary collection of files. A catalog file contains a collection of cryptographic hashes, or *thumbprints*. Each thumbprint corresponds to a file that is included in the collection.

Plug and Play (PnP) device installation recognizes the signed catalog file of a [driver package](driver-packages.md) as the [digital signature](digital-signatures.md) for the driver package, where each thumbprint in the catalog file corresponds to a file that is installed by the driver package. Regardless of the intended operating system, cryptographic technology is used to digitally-sign the catalog file.

PnP device installation considers the digital signature of a [driver package](driver-packages.md) to be invalid if any file in the driver package is altered after the driver package was signed. Such files include the INF file, the catalog file, and all files that are copied by **[INF CopyFiles directives](inf-copyfiles-directive.md)**. For example, even a single-byte change to correct a misspelling invalidates the digital signature. If the digital signature is invalid, you must either resubmit the driver package to the [Windows Hardware Quality Labs (WHQL)](/previous-versions/windows/hardware/hck/jj124227(v=vs.85)) for a new signature or generate a new [Authenticode](authenticode.md) signature for the driver package.

Similarly, changes to a device's hardware or firmware require a revised [device ID](device-ids.md) value so that the system can detect the updated device and install the correct driver. Because the revised device ID value must appear in the INF file, you must either resubmit the package to WHQL for a new signature or generate a new [Authenticode](authenticode.md) signature for the driver package. You must do this even if the driver binaries do not change.

The **CatalogFile** directive in the **[INF Version section](inf-version-section.md)** of the driver's [INF file](overview-of-inf-files.md) specifies the name of the catalog file for the driver package. During driver installation, the operating system uses the **CatalogFile** directive to identify and validate the catalog file. The system installs the catalog file to the CatRoot directory under the system directory returned by [GetSystemDirectory](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemdirectoryw), e.g. *%SystemRoot%\\System32\\CatRoot*. Note that catalog files should not be added to or removed from that directory manually.  For driver packages, the catalog file will be automatically installed to the CatRoot when the driver package is staged to the Driver Store and will be automatically uninstalled from the CatRoot when the driver package is removed from the Driver Store. If you need to install a catalog file to the CatRoot for reasons outside of a driver package, see [Installing a Catalog File by using SignTool](installing-a-catalog-file-by-using-signtool.md) and [Installing a Catalog File by using CryptCATAdminAddCatalog](installing-a-catalog-file-by-using-cryptcatadminaddcatalog.md).

### Guidelines for Catalog Files

Starting with Windows 2000, if the [driver package](driver-packages.md) installs the same binaries on all versions of Windows, the INF file can contain a single, undecorated **CatalogFile** directive. However, if the package installs different binaries for different versions of Windows, the INF file should contain decorated **CatalogFile** directives. For more information about the **CatalogFile** directive, see **[INF Version Section](inf-version-section.md)**.

If you have more than one driver package, you should create a separate catalog file for each driver package and give each catalog file a unique file name. Two unrelated driver packages cannot share a single catalog file. However, a single driver package that serves multiple devices requires only one catalog file.
