---
title: Certificate Stores
description: Certificate Stores
keywords:
- certificate stores WDK
ms.date: 09/16/2024
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
   

## What are Service Account Certificate Stores?

Service account certificate stores are specialized certificate stores used by service accounts in Windows. These stores are distinct from the Local Machine and Current User certificate stores and are used to manage certificates for services running under specific service accounts.

### Types of Service Accounts

1. **LocalService**: A predefined local account used by the service control manager.
2. **NetworkService**: A predefined local account that has more privileges than LocalService.

### Using Certificates Management Console

To manage certificates for a service account, you can use the Certificates management console with a custom configuration. This allows you to add multiple snap-ins and save the console as a .msc file for later use.


### When to use Service Account Certificate Stores

1. **Service-Specific Certificates**: When a certificate is required for a service running under a specific service account, it should be stored in the service account's certificate store.
2. **Security Isolation**: To ensure that certificates are only accessible to the service that requires them, enhancing security by isolating the certificate usage to the service account.

### When not to use Service Account Certificate Stores

1. **General Use Certificates**: Certificates that need to be accessed by multiple services or users should be stored in the Local Machine or Current User certificate stores.
2. **Complex Management**: If managing certificates for multiple service accounts becomes too complex, it might be more practical to use the Local Machine certificate store and manage permissions accordingly.

### Adding Certificates to Service Account Stores

One approach is to log in interactively under the service account to import the certificate.

Another method is to install the certificate in the LocalMachine\My store and grant private key read permissions to the service account.

## Additional Resources  
   
For more information on specific certificate stores, see the following topics:  
   
- [Local Machine and Current User Certificate Stores](local-machine-and-current-user-certificate-stores.md)  
- [Trusted Root Certification Authorities Certificate Store](trusted-root-certification-authorities-certificate-store.md)  
- [Trusted Publishers Certificate Store](trusted-publishers-certificate-store.md)  
   
By understanding where the certificate store is located and how to use its contents, you can effectively manage certificates on your Windows computer.
