MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read a blog, "p" to create a post, or "q" to quit:'

blogs = dict()

def menu():
    # Show the user the available blogs
    # Let user make choice
    # Do something with choice
    # Exit

    print_blogs()
    selection = input(MENU_PROMPT)

def print_blogs():
    for key, blog in blogs.items(): # [(blog_name, Blog), (blog_name, Blog)]
        print('- {}'.format(blog))