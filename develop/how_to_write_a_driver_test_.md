How to write a driver test using a Driver Test template
==============================================================================================================

You can use the Windows Driver Kit (WDK) for Windows 8 to create your own driver tests or to customize some of the tests that are provided. You can deploy the tests that you create to remote test computers using the driver testing framework that the WDK provides for Microsoft Visual Studio Ultimate 2012.

The WDK provides templates that create starter code for a Windows Driver test project in C++, C\#, and Script (JScript). You can select the test cases that you want to include, or you can start with a blank project. You can customize the code to add new test cases for your driver. You can deploy your tests from Visual Studio using the driver test framework.

<span id="To_customize_a_driver_test_using_the_Driver_Test_template_for_C__"></span><span id="to_customize_a_driver_test_using_the_driver_test_template_for_c__"></span><span id="TO_CUSTOMIZE_A_DRIVER_TEST_USING_THE_DRIVER_TEST_TEMPLATE_FOR_C__"></span>To customize a driver test using the Driver Test template for C++
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  From the **File** menu, click **New &gt; Project**.
2.  From the list of installed templates in the **New Project** dialog box, select **Visual C++ &gt; Windows Driver &gt; Tests**.
3.  Select **Windows Driver Test in C++**.
4.  Provide a name for your driver test project and a location (or use the default).
5.  From the **Windows Driver Test** dialog box, select the test cases that you want to include or choose an empty (blank) driver test. For more information about the test cases, see [Windows Driver test cases](#windows_driver_test_cases).
6.  Add the required test metadata. For more information, see [How to add test metadata](to_add_test_metadata.md).
7.  Build your driver test.

<span id="To_customize_a_driver_test_using_the_Driver_Test_template_for_C_"></span><span id="to_customize_a_driver_test_using_the_driver_test_template_for_c_"></span><span id="TO_CUSTOMIZE_A_DRIVER_TEST_USING_THE_DRIVER_TEST_TEMPLATE_FOR_C_"></span>To customize a driver test using the Driver Test template for C\#
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  From the **File** menu, click **New &gt; Project**.
2.  From the list of installed templates in the **New Project** dialog box, select **Visual C\# &gt; Windows Driver** .
3.  Select **Windows Driver Test in C\#**.
4.  Provide a name for your driver test project and a location (or use the default).
5.  From the **Windows Driver Test** dialog box, select the test cases that you want to include or choose an empty (blank) driver test. For information about the test cases, see [Windows Driver test cases](#windows_driver_test_cases).
6.  Add the required test metadata. For more information, see [How to add test metadata](to_add_test_metadata.md).
7.  Build your driver test.

<span id="To_customize_a_driver_test_using_the_Driver_Test_template_for_Script"></span><span id="to_customize_a_driver_test_using_the_driver_test_template_for_script"></span><span id="TO_CUSTOMIZE_A_DRIVER_TEST_USING_THE_DRIVER_TEST_TEMPLATE_FOR_SCRIPT"></span>To customize a driver test using the Driver Test template for Script
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  From the **File** menu, click **New &gt; Project**.
2.  From the list of installed templates in the **New Project** dialog box, select **Script &gt; Windows Driver** .
3.  Select **Windows Driver Test Script**.
4.  Provide a name for your driver test project and a location (or use the default).
5.  From the **Windows Driver Test** dialog box, select the test cases that you want to include or choose an empty (blank) driver test. For information about the test cases, see [Windows Driver test cases](#windows_driver_test_cases).
6.  Add the required test metadata. For more information, see [How to add test metadata](to_add_test_metadata.md).
7.  Build your driver test.

<span id="Making_the_driver_tests_you_create_available_for_deployment_on_test_computers"></span><span id="making_the_driver_tests_you_create_available_for_deployment_on_test_computers"></span><span id="MAKING_THE_DRIVER_TESTS_YOU_CREATE_AVAILABLE_FOR_DEPLOYMENT_ON_TEST_COMPUTERS"></span>Making the driver tests you create available for deployment on test computers
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When you build your driver test, the new test will be available for deployment to a test computer. By default, the tests that you create will appear in the test category **My Test Category**. The names of the tests are based upon the test cases that you choose, and they will have names such as **My Plug and Play Surprise Remove Test**. During each build of the test, the test will be overwritten. The latest build of the test will be available to deploy and run on the test computer.

<span id="windows_driver_test_cases"></span><span id="WINDOWS_DRIVER_TEST_CASES"></span>Windows Driver test cases
-----------------------------------------------------------------------------------------------------------------

The WDK provides starter code for a Windows Driver test project in C++, C\#, and Script. You can select test cases that you want to include, or you can start with a blank project. Not all test cases are available in every language.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Plug and Play Test Cases</th>
<th align="left">Test cases that force a driver to handle most of the Plug and Play (PnP)-related IRPs</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Disable/Enable</td>
<td align="left">Provides code for test cases that disable and enable a PnP device.</td>
</tr>
<tr class="even">
<td align="left">Remove</td>
<td align="left">Provides code for test cases that remove a PnP device.</td>
</tr>
<tr class="odd">
<td align="left">Surprise Remove</td>
<td align="left">Provides code for test cases that perform a surprise remove of a PnP device.</td>
</tr>
<tr class="even">
<td align="left">Power Management Test Cases</td>
<td align="left">Provides test cases that force a driver to handle system sleep states.</td>
</tr>
<tr class="odd">
<td align="left">System Sleep States</td>
<td align="left">Provides code for test cases that perform device I/O while the system cycles through sleep and power state.</td>
</tr>
<tr class="even">
<td align="left">Stress and Functionality Test Cases</td>
<td align="left">Provides test cases that perform I/O stress and function testing of IOCTL and WMI interfaces.</td>
</tr>
<tr class="odd">
<td align="left">I/O Stress</td>
<td align="left">Provides test cases that perform device I/O stress.</td>
</tr>
<tr class="even">
<td align="left">Functional IOCTL Interface</td>
<td align="left">Provides a template for creating functional test cases for the IOCTL interface. (only available for C++ ).</td>
</tr>
<tr class="odd">
<td align="left">Functional WMI Interface</td>
<td align="left">Provides a template for creating functional test cases for the Windows Management Interface (WMI). (only available in Script)</td>
</tr>
<tr class="even">
<td align="left">Empty Test Case</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left">Provides a blank template for creating a Windows Driver test project.</td>
</tr>
</tbody>
</table>

 

<span id="related_topics"></span>Related topics
-----------------------------------------------

* [Test Authoring and Execution Framework](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh439725)
* [Windows Driver Testing Framework](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff539547)
* [How to add test metadata](to_add_test_metadata.md)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[VsDriver\vsdriver]:%20How%20to%20write%20a%20driver%20test%20using%20a%20Driver%20Test%20template%20%20RELEASE:%20%289/30/2015%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default. "Send comments about this topic to Microsoft")


