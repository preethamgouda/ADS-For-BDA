class BrowserNavigation:
    def __init__(self):
        self.back_stack = []       # Stack for backward navigation history
        self.forward_stack = []    # Stack for forward navigation history
        self.current_page = None   # Current page URL

    def navigate_to(self, page_url):
        if self.current_page:
            self.back_stack.append(self.current_page)
            self.forward_stack = []  # Clear the forward stack when navigating to a new page
        self.current_page = page_url

    def go_back(self):
        if not self.back_stack:
            print("Cannot go back. Backward history is empty.")
            return
        self.forward_stack.append(self.current_page)
        self.current_page = self.back_stack.pop()

    def go_forward(self):
        if not self.forward_stack:
            print("Cannot go forward. Forward history is empty.")
            return
        self.back_stack.append(self.current_page)
        self.current_page = self.forward_stack.pop()

    def current_page_url(self):
        return self.current_page

    def print_navigation_history(self):
        print("Backward History:", self.back_stack)
        print("Forward History:", self.forward_stack)


# Example usage:
browser_navigation = BrowserNavigation()

browser_navigation.navigate_to("https://www.example.com")
browser_navigation.navigate_to("https://www.openai.com")
browser_navigation.navigate_to("https://www.github.com")

browser_navigation.print_navigation_history()  # Print navigation history

print("Current Page URL:", browser_navigation.current_page_url())  # Print the current page URL

browser_navigation.go_back()
print("Current Page URL (after going back):", browser_navigation.current_page_url())

browser_navigation.go_forward()
print("Current Page URL (after going forward):", browser_navigation.current_page_url())

browser_navigation.print_navigation_history()  # Print updated navigation history
