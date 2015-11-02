Target platform on MSDN driver reference pages
===================================================================================================================

In the Requirements block at the bottom of MSDN driver reference pages, you'll see an entry called **Target Platform**. This line lists editions of Windows to which the page applies.

Here's an example of such an entry:

![Target Platform set to universal in Requirements block](images/TargetPlatform.png)

The values specified in **Target Platform** map to the values you can use in Visual Studio, in the **Target Platform** property under **Configuration Properties-&gt;Driver** .

Here are the values you might see for **Target Platform** on MSDN, and what they mean:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Term</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="Universal"></span><span id="universal"></span><span id="UNIVERSAL"></span>Universal</p></td>
<td align="left"><p>A Universal Windows driver can call this device driver interface (DDI).</p>
<p>A Universal Windows driver runs on the following Universal Windows Platform (UWP)-based editions of Windows 10:</p>
<ul>
<li>Windows 10 for desktop editions (Home, Pro, and Enterprise)</li>
<li>Windows 10 Mobile</li>
<li>Windows 10 IoT Core</li>
<li>Windows Server 2016 Technical Preview</li>
</ul>
<p>For more info, see <a href="getting_started_with_universal_drivers.md">Getting Started with Universal Windows drivers</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Desktop"></span><span id="desktop"></span><span id="DESKTOP"></span>Desktop</p></td>
<td align="left"><p>A driver for Windows 10 for desktop editions or Windows Server 2016 Technical Preview can call this DDI.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Mobile"></span><span id="mobile"></span><span id="MOBILE"></span>Mobile</p></td>
<td align="left"><p>A driver for Windows 10 Mobile can call this DDI.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[VsDriver\vsdriver]:%20Target%20platform%20on%20MSDN%20driver%20reference%20pages%20%20RELEASE:%20%289/30/2015%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default. "Send comments about this topic to Microsoft")


