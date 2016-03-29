---
title: Install the driver and sample app
description: This section provides information on installing the driver and the WSD sample app.
ms.assetid: BF89F0D0-2ED3-4900-996F-BB7B9C8C9B80
---

# Install the driver and sample app


This section provides information on installing the driver and the WSD sample app.

## Install the driver on a Windows 8.1 machine


To install the print driver included in the 3D printing SDK, selecting the driver's .inf file, right-click on the file, and then select **Install**.

## Install the sample app


Start by installing Microsoft Visual Studio 2013 (Professional or Ultimate) and applying any required service packs or updates.

The sample implementation consists of an Microsoft Internet Information Services (IIS) web service implemented in ASP.NET with a http handler that responds to the WS-Print protocol requests.

Directed discovery can operate with the web service running as it works off the http protocol without UDP discovery.

### Installation requirements

Deployment of the web service on a windows machine requires that the machine have IIS and ASP.NET installed along with Microsoft .NET 4.5.

### Install IIS

1.  To install IIS, press the **Windows** + **R** key combination to bring up a **Run** dialog box, then type `appwiz.cpl` and press **Enter**.

    ![run](images/wsd-app-1.png)

    This will open Control Panel **Programs and Features**.

2.  On the **Control Panel Home** pane, click **Turn Windows features on or off**.

    ![programs and features](images/wsd-app-2.png)

3.  In the **Windows Features** dialog, select the **Internet Information Services** check box.

    ![windows features](images/wsd-app-3.png)

4.  Expand the **Internet Information Services** check box and expand **World Wide Web Services**.

    ![world wide web services](images/wsd-app-4.png)

5.  Expand **Application Development Features** and select and the sub-features shown here:

    ![application development features](images/wsd-app-5.png)

6.  Click **OK**. The **Applying changes** dialog will show the progress of the installation.

    ![applying changes](images/wsd-app-6.png)

7.  When the **Applying changes** dialog closes, open a browser and navigate to http://localhost.

    ![localhost](images/wsd-app-7.png)

### Publish the project

Publish the Handler project to localhost to deploy the web service.

![publish web](images/wsd-app-8.png)

Once publishing is successful, browsing to http://localhost will result in an empty file being sent back. If the handler is not setup correctly, you will receive an error message or potentially see the default IIS web page.

You can switch the **DefaultAppPool** to run with the **NetworkService** identity and it will continue to work as expected. **DefaultAppPool** should also work across the network as well.

### Verify site bindings

if you need to support IPv6, ensure that the ASP.NET site bindings are created for IPv6.

The Handler project publishes the project to **Default Web Site**.

By default, the site is bound to port 80 on all IP addresses.

![site bindings](images/wsd-app-9.png)

### Update Windows Firewall

By default, Windows blocks port 80 on a machine, so you will need to update Windows Firewall to allow World Wide Web Services (http) traffic inbound. Without turning this on, incoming http requests from clients will fail.

![windows firewall](images/wsd-app-10.png)

### Install the Fabrikam Printer

### Directed Discovery via Http endpoint

1.  Open **Devices and Printers** in **Control Panel**.

2.  Select **Add a printer**.

3.  Select **The printer I want isn't listed**.

    ![add printer](images/wsd-app-11.png)

4.  Select **Add a printer using TCP/IP address or hostname**.

    ![find a printer by other options](images/wsd-app-12.png)

5.  Select **Web Services Device** from **Device type** list.

    ![select device type](images/wsd-app-13.png)

6.  Type a hostname or IP address and click **Next**.

    The **Contacting printer...** progress bar will appear.

    ![enter hostname or ip address](images/wsd-app-14.png)

    When the Fabrikam printer is installed the following message will display:

    ![fabrikam 3d printer installed](images/wsd-app-15.png)

### Ad-Hoc Discovery via UDP Multicast

Ad-hoc discovery can be performed by implementing a UDP server that listens to discovery events on port 3702.

For more information on the exchange sequence, see [Discovery and Metadata Exchange Message Patterns](http://msdn.microsoft.com/library/windows/desktop/bb513677.aspx).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Install%20the%20driver%20and%20sample%20app%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




