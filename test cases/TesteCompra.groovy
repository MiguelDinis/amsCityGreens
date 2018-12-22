import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.checkpoint.CheckpointFactory as CheckpointFactory
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as MobileBuiltInKeywords
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testcase.TestCaseFactory as TestCaseFactory
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testdata.TestDataFactory as TestDataFactory
import com.kms.katalon.core.testobject.ObjectRepository as ObjectRepository
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WSBuiltInKeywords
import com.kms.katalon.core.webui.driver.DriverFactory as DriverFactory
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUiBuiltInKeywords
import internal.GlobalVariable as GlobalVariable
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS

import com.thoughtworks.selenium.Selenium
import org.openqa.selenium.firefox.FirefoxDriver
import org.openqa.selenium.WebDriver
import com.thoughtworks.selenium.webdriven.WebDriverBackedSelenium
import static org.junit.Assert.*
import java.util.regex.Pattern
import static org.apache.commons.lang3.StringUtils.join

WebUI.openBrowser('https://www.katalon.com/')
def driver = DriverFactory.getWebDriver()
String baseUrl = "https://www.katalon.com/"
selenium = new WebDriverBackedSelenium(driver, baseUrl)
selenium.open("http://amscitygreens.pythonanywhere.com/")
selenium.click("link=Log-in")
selenium.click("id=id_username")
selenium.type("id=id_username", "User1")
selenium.click("id=content")
selenium.click("id=id_password")
selenium.type("id=id_password", "123user")
selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[4]")
selenium.click("link=Shop")
selenium.click("link=Season baskets")
selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='Big vegetables basket'])[1]/following::img[1]")
selenium.select("id=id_quantity", "label=2")
selenium.click("id=id_quantity")
selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='Quantity:'])[1]/following::input[3]")
selenium.click("link=Checkout")
selenium.click("id=id_first_name")
selenium.type("id=id_first_name", "new")
selenium.click("id=id_last_name")
selenium.type("id=id_last_name", "user")
selenium.click("id=id_email")
selenium.type("id=id_email", "newuser@gmail.com")
selenium.click("id=id_address")
selenium.type("id=id_address", "rua do gravito")
selenium.click("id=id_postal_code")
selenium.type("id=id_postal_code", "3100")
selenium.click("id=id_city")
selenium.type("id=id_city", "Aveiro")
selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='City:'])[1]/following::input[2]")
selenium.click("name=submit")
selenium.click("id=email")
selenium.click("id=password")
selenium.type("id=password", "123456789")
selenium.click("id=btnLogin")
selenium.click("xpath=(.//*[normalize-space(text()) and normalize-space(.)='Add a debit or credit card'])[1]/following::button[1]")
selenium.click("id=confirmButtonTop")
selenium.click("id=merchantReturnBtn")
