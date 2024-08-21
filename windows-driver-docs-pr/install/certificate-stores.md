---
title: Certificate Stores
description: Certificate Stores
keywords:
- certificate stores WDK
ms.date: 08/20/2024
ai-usage: ai-assisted
---

# Certificate Stores  
   
Windows stores certificates locally on the computer in a storage location called the *certificate store*. A certificate store often has numerous certificates, possibly issued from a number of different certification authorities (CAs).  
   
## Where is the Certificate Store Located?  
   
The certificate store is located within the Windows operating system and can be accessed using various tools and methods. There are two primary types of certificate stores:  
   
1. **Local Machine Certificate Store**: This store contains certificates that are accessible to all users on the computer. It is located in the system registry under `HKEY_LOCAL_MACHINE`.  
   
2. **Current User Certificate Store**: This store contains certificates that are accessible only to the current user. It is located in the system registry under `HKEY_CURRENT_USER`.  
   
## How to Use the Contents of the Certificate Store  
   
To use the contents of the certificate store, you can perform various actions such as viewing, importing, exporting, and managing certificates. Here are some common tasks:  
   
### Viewing Certificates  
   
You can view the certificates in the certificate store using the Microsoft Management Console (MMC) snap-in. Follow these steps:  
   
1. Press `Win + R`, type `mmc`, and press `Enter`.  
2. In the MMC console, go to `File` > `Add/Remove Snap-in`.  
3. Select `Certificates` and click `Add`.  
4. Choose either `Computer account` for the Local Machine store or `My user account` for the Current User store, and click `Finish`.  
5. Click `OK` to close the snap-in window.  
6. Expand the `Certificates` node to view the certificates in the store.  
   
For detailed instructions, see [How to: View certificates with the MMC snap-in](/dotnet/framework/wcf/feature-details/how-to-view-certificates-with-the-mmc-snap-in).  
   
### Importing Certificates  
   
To import a certificate into the certificate store:  
   
1. Open the MMC console and add the `Certificates` snap-in as described above.  
2. Right-click on the appropriate certificate store (e.g., `Personal`), select `All Tasks`, and then `Import`.  
3. Follow the Certificate Import Wizard to select and import the certificate file.  
   
### Exporting Certificates  
   
To export a certificate from the certificate store:  
   
1. Open the MMC console and add the `Certificates` snap-in as described above.  
2. Right-click on the certificate you want to export, select `All Tasks`, and then `Export`.  
3. Follow the Certificate Export Wizard to export the certificate to a file.  
   
### Managing Certificates  
   
You can manage certificates by performing tasks such as deleting expired certificates, renewing certificates, and configuring certificate properties. These actions can be done through the MMC console or programmatically using Windows APIs.  
   
## Additional Resources  
   
For more information on specific certificate stores, see the following topics:  
   
- [Local Machine and Current User Certificate Stores](local-machine-and-current-user-certificate-stores.md)  
- [Trusted Root Certification Authorities Certificate Store](trusted-root-certification-authorities-certificate-store.md)  
- [Trusted Publishers Certificate Store](trusted-publishers-certificate-store.md)  
   
By understanding where the certificate store is located and how to use its contents, you can effectively manage certificates on your Windows computer.
