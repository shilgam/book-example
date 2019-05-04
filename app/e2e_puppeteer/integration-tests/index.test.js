const assert = require('assert')
const puppeteer = require('puppeteer')

let browser
let page

const DEBUG_MODE = process.argv.includes('--debugMode');

const debugLaunchOptions = DEBUG_MODE ? {
  headless: false,
  slowMo: 100,
} : {};

console.log(`>>> debugLaunchOptions: ${JSON.stringify(debugLaunchOptions)}`)

before(async() => {
  browser = await puppeteer.launch({
    args: [
      // Required for Docker version of Puppeteer
      '--no-sandbox',
      '--disable-setuid-sandbox',
      // This will write shared memory files into /tmp instead of /dev/shm,
      // because Docker’s default for /dev/shm is 64MB
      '--disable-dev-shm-usage',
    ],
    ...debugLaunchOptions,
  })

  const browserVersion = await browser.version()
  console.log(`Started ${browserVersion}`)
})

beforeEach(async() => {
  page = await browser.newPage()
})

afterEach(async() => {
  await page.close()
})

after(async() => {
  await browser.close()
})

describe('App', () => {
  it('renders', async() => {
    const response = await page.goto('http://google.com/')
    assert(response.ok())
    await page.screenshot({ path: `./screenshots/app.png` })
  })
})
