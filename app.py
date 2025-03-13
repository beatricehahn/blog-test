blogs = dict()

def menu():
    # Show the user the available blogs
    # Let user make choice
    # Do something with choice
    # Exit

    print_blogs()

def print_blogs():
    for key, blog in blogs.items(): # [(blog_name, Blog), (blog_name, Blog)]
        print('- {}'.format(blog))