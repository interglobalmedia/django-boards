import paginationScrollBehavior from './django-boards-pagination.js'
import {
  scrollTop,
  scrollStep,
  scrollTopButton,
  scrollDownButton,
} from './scroll-top-bottom.js'
import toggleVisibilityScrollTop from './visibility-top.js'
import toggleVisibilityScrollBottom from './visibility-bottom.js'
import { copyButton } from './copy-button.js'

// const copyLinkInit = copyLink
const toggleVisibilityScrollTopInit = toggleVisibilityScrollTop()
const toggleVisibilityScrollBottomInit = toggleVisibilityScrollBottom()
const paginationScrollBehaviorInit = paginationScrollBehavior()
const copyButtonInit = copyButton()

// For scroll to top functionality

scrollTopButton.addEventListener('pointerdown', scrollTop)

// Scroll to bottom functionality

scrollDownButton.addEventListener('pointerdown', scrollStep)