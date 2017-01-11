import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE','blog_project.settings')

import django
django.setup()

from blog.models import Article, Detail

def populate():
    article_1 = [
         {"content": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eu ligula ut mauris facilisis porta ac in ipsum. Ut pulvinar eget nulla at eleifend. Vivamus euismod urna molestie, convallis ipsum sed, tristique justo. Sed egestas nulla eu tortor blandit, id tempus sem dictum. Vestibulum dictum euismod dolor sed pharetra. Morbi ornare pulvinar metus, eu sagittis ligula hendrerit vel. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras sit amet mollis dui. Etiam dolor sapien, dictum at est eget, aliquam sagittis nibh. Proin eu ex non augue luctus ultrices. Aliquam dictum id tortor aliquet pellentesque. Donec dolor felis, placerat at fermentum in, pharetra nec augue. Aliquam mollis nibh nec nibh iaculis mollis. Curabitur lectus velit, feugiat at sem et, malesuada dictum quam.

Duis lectus magna, vestibulum sed blandit quis, vulputate ac augue. Fusce hendrerit rhoncus viverra. Quisque lacinia nec ipsum quis blandit. Sed magna purus, ullamcorper quis laoreet sit amet, pretium ac erat. Nam accumsan commodo leo at bibendum. Mauris in mollis ipsum. Etiam lectus nisi, commodo vitae urna at, fermentum lacinia sem. Sed suscipit risus dolor, nec pulvinar tellus porttitor ut. Praesent ullamcorper mattis hendrerit. Praesent euismod leo magna, ac molestie mi egestas nec. Cras suscipit turpis sed erat finibus, ut sodales leo eleifend. Morbi vehicula, orci sit amet consectetur viverra, ex odio pharetra massa, eu porta turpis lacus vel nisi. Cras ac venenatis turpis. Suspendisse consectetur augue nisi, a ornare massa auctor euismod. Nam diam ipsum, hendrerit quis gravida vitae, molestie vitae ante. In dictum sit amet nulla vel gravida.

Morbi vulputate tempor sapien at vulputate. Nulla eget sapien quis lectus fringilla pretium at quis ante. In purus libero, lacinia nec rutrum in, finibus sit amet arcu. Praesent elit odio, luctus non faucibus vitae, eleifend tincidunt urna. Sed lobortis massa in ligula euismod feugiat. Maecenas commodo, mi et posuere sollicitudin, nisl lacus dictum magna, vestibulum euismod arcu est ut elit. Pellentesque ultrices magna enim, id volutpat odio vulputate in. Mauris magna lectus, mattis suscipit ultrices auctor, dapibus vitae dui. Nullam mattis elementum sollicitudin. Fusce viverra tempus odio in hendrerit. Curabitur euismod, lacus nec venenatis porta, velit justo varius justo, quis iaculis enim urna et lacus. Etiam suscipit tempor nisi vitae sagittis. Suspendisse tincidunt, augue non semper convallis, urna arcu facilisis massa, sed elementum ligula dui ac neque.''',
         "description":"this is description of article 1",
         "views":5,
         "likes":3}]

    article_2 = [
         {"content": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eu ligula ut mauris facilisis porta ac in ipsum. Ut pulvinar eget nulla at eleifend. Vivamus euismod urna molestie, convallis ipsum sed, tristique justo. Sed egestas nulla eu tortor blandit, id tempus sem dictum. Vestibulum dictum euismod dolor sed pharetra. Morbi ornare pulvinar metus, eu sagittis ligula hendrerit vel. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras sit amet mollis dui. Etiam dolor sapien, dictum at est eget, aliquam sagittis nibh. Proin eu ex non augue luctus ultrices. Aliquam dictum id tortor aliquet pellentesque. Donec dolor felis, placerat at fermentum in, pharetra nec augue. Aliquam mollis nibh nec nibh iaculis mollis. Curabitur lectus velit, feugiat at sem et, malesuada dictum quam.

Duis lectus magna, vestibulum sed blandit quis, vulputate ac augue. Fusce hendrerit rhoncus viverra. Quisque lacinia nec ipsum quis blandit. Sed magna purus, ullamcorper quis laoreet sit amet, pretium ac erat. Nam accumsan commodo leo at bibendum. Mauris in mollis ipsum. Etiam lectus nisi, commodo vitae urna at, fermentum lacinia sem. Sed suscipit risus dolor, nec pulvinar tellus porttitor ut. Praesent ullamcorper mattis hendrerit. Praesent euismod leo magna, ac molestie mi egestas nec. Cras suscipit turpis sed erat finibus, ut sodales leo eleifend. Morbi vehicula, orci sit amet consectetur viverra, ex odio pharetra massa, eu porta turpis lacus vel nisi. Cras ac venenatis turpis. Suspendisse consectetur augue nisi, a ornare massa auctor euismod. Nam diam ipsum, hendrerit quis gravida vitae, molestie vitae ante. In dictum sit amet nulla vel gravida.

Morbi vulputate tempor sapien at vulputate. Nulla eget sapien quis lectus fringilla pretium at quis ante. In purus libero, lacinia nec rutrum in, finibus sit amet arcu. Praesent elit odio, luctus non faucibus vitae, eleifend tincidunt urna. Sed lobortis massa in ligula euismod feugiat. Maecenas commodo, mi et posuere sollicitudin, nisl lacus dictum magna, vestibulum euismod arcu est ut elit. Pellentesque ultrices magna enim, id volutpat odio vulputate in. Mauris magna lectus, mattis suscipit ultrices auctor, dapibus vitae dui. Nullam mattis elementum sollicitudin. Fusce viverra tempus odio in hendrerit. Curabitur euismod, lacus nec venenatis porta, velit justo varius justo, quis iaculis enim urna et lacus. Etiam suscipit tempor nisi vitae sagittis. Suspendisse tincidunt, augue non semper convallis, urna arcu facilisis massa, sed elementum ligula dui ac neque.''',
         "description":"this is description of article 2",
         "views":7,
         "likes":6}]

    article_3 = [
              {"content": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eu ligula ut mauris facilisis porta ac in ipsum. Ut pulvinar eget nulla at eleifend. Vivamus euismod urna molestie, convallis ipsum sed, tristique justo. Sed egestas nulla eu tortor blandit, id tempus sem dictum. Vestibulum dictum euismod dolor sed pharetra. Morbi ornare pulvinar metus, eu sagittis ligula hendrerit vel. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras sit amet mollis dui. Etiam dolor sapien, dictum at est eget, aliquam sagittis nibh. Proin eu ex non augue luctus ultrices. Aliquam dictum id tortor aliquet pellentesque. Donec dolor felis, placerat at fermentum in, pharetra nec augue. Aliquam mollis nibh nec nibh iaculis mollis. Curabitur lectus velit, feugiat at sem et, malesuada dictum quam.

     Duis lectus magna, vestibulum sed blandit quis, vulputate ac augue. Fusce hendrerit rhoncus viverra. Quisque lacinia nec ipsum quis blandit. Sed magna purus, ullamcorper quis laoreet sit amet, pretium ac erat. Nam accumsan commodo leo at bibendum. Mauris in mollis ipsum. Etiam lectus nisi, commodo vitae urna at, fermentum lacinia sem. Sed suscipit risus dolor, nec pulvinar tellus porttitor ut. Praesent ullamcorper mattis hendrerit. Praesent euismod leo magna, ac molestie mi egestas nec. Cras suscipit turpis sed erat finibus, ut sodales leo eleifend. Morbi vehicula, orci sit amet consectetur viverra, ex odio pharetra massa, eu porta turpis lacus vel nisi. Cras ac venenatis turpis. Suspendisse consectetur augue nisi, a ornare massa auctor euismod. Nam diam ipsum, hendrerit quis gravida vitae, molestie vitae ante. In dictum sit amet nulla vel gravida.

     Morbi vulputate tempor sapien at vulputate. Nulla eget sapien quis lectus fringilla pretium at quis ante. In purus libero, lacinia nec rutrum in, finibus sit amet arcu. Praesent elit odio, luctus non faucibus vitae, eleifend tincidunt urna. Sed lobortis massa in ligula euismod feugiat. Maecenas commodo, mi et posuere sollicitudin, nisl lacus dictum magna, vestibulum euismod arcu est ut elit. Pellentesque ultrices magna enim, id volutpat odio vulputate in. Mauris magna lectus, mattis suscipit ultrices auctor, dapibus vitae dui. Nullam mattis elementum sollicitudin. Fusce viverra tempus odio in hendrerit. Curabitur euismod, lacus nec venenatis porta, velit justo varius justo, quis iaculis enim urna et lacus. Etiam suscipit tempor nisi vitae sagittis. Suspendisse tincidunt, augue non semper convallis, urna arcu facilisis massa, sed elementum ligula dui ac neque.''',
              "description":"this is description of article 3",
              "views":36,
              "likes":15}]
    article_4 = [
         {"content": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eu ligula ut mauris facilisis porta ac in ipsum. Ut pulvinar eget nulla at eleifend. Vivamus euismod urna molestie, convallis ipsum sed, tristique justo. Sed egestas nulla eu tortor blandit, id tempus sem dictum. Vestibulum dictum euismod dolor sed pharetra. Morbi ornare pulvinar metus, eu sagittis ligula hendrerit vel. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras sit amet mollis dui. Etiam dolor sapien, dictum at est eget, aliquam sagittis nibh. Proin eu ex non augue luctus ultrices. Aliquam dictum id tortor aliquet pellentesque. Donec dolor felis, placerat at fermentum in, pharetra nec augue. Aliquam mollis nibh nec nibh iaculis mollis. Curabitur lectus velit, feugiat at sem et, malesuada dictum quam.

Duis lectus magna, vestibulum sed blandit quis, vulputate ac augue. Fusce hendrerit rhoncus viverra. Quisque lacinia nec ipsum quis blandit. Sed magna purus, ullamcorper quis laoreet sit amet, pretium ac erat. Nam accumsan commodo leo at bibendum. Mauris in mollis ipsum. Etiam lectus nisi, commodo vitae urna at, fermentum lacinia sem. Sed suscipit risus dolor, nec pulvinar tellus porttitor ut. Praesent ullamcorper mattis hendrerit. Praesent euismod leo magna, ac molestie mi egestas nec. Cras suscipit turpis sed erat finibus, ut sodales leo eleifend. Morbi vehicula, orci sit amet consectetur viverra, ex odio pharetra massa, eu porta turpis lacus vel nisi. Cras ac venenatis turpis. Suspendisse consectetur augue nisi, a ornare massa auctor euismod. Nam diam ipsum, hendrerit quis gravida vitae, molestie vitae ante. In dictum sit amet nulla vel gravida.

Morbi vulputate tempor sapien at vulputate. Nulla eget sapien quis lectus fringilla pretium at quis ante. In purus libero, lacinia nec rutrum in, finibus sit amet arcu. Praesent elit odio, luctus non faucibus vitae, eleifend tincidunt urna. Sed lobortis massa in ligula euismod feugiat. Maecenas commodo, mi et posuere sollicitudin, nisl lacus dictum magna, vestibulum euismod arcu est ut elit. Pellentesque ultrices magna enim, id volutpat odio vulputate in. Mauris magna lectus, mattis suscipit ultrices auctor, dapibus vitae dui. Nullam mattis elementum sollicitudin. Fusce viverra tempus odio in hendrerit. Curabitur euismod, lacus nec venenatis porta, velit justo varius justo, quis iaculis enim urna et lacus. Etiam suscipit tempor nisi vitae sagittis. Suspendisse tincidunt, augue non semper convallis, urna arcu facilisis massa, sed elementum ligula dui ac neque.''',
         "description":"this is description of article 4",
         "views":64,
         "likes":45}]

    article_5 = [
         {"content": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eu ligula ut mauris facilisis porta ac in ipsum. Ut pulvinar eget nulla at eleifend. Vivamus euismod urna molestie, convallis ipsum sed, tristique justo. Sed egestas nulla eu tortor blandit, id tempus sem dictum. Vestibulum dictum euismod dolor sed pharetra. Morbi ornare pulvinar metus, eu sagittis ligula hendrerit vel. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras sit amet mollis dui. Etiam dolor sapien, dictum at est eget, aliquam sagittis nibh. Proin eu ex non augue luctus ultrices. Aliquam dictum id tortor aliquet pellentesque. Donec dolor felis, placerat at fermentum in, pharetra nec augue. Aliquam mollis nibh nec nibh iaculis mollis. Curabitur lectus velit, feugiat at sem et, malesuada dictum quam.

Duis lectus magna, vestibulum sed blandit quis, vulputate ac augue. Fusce hendrerit rhoncus viverra. Quisque lacinia nec ipsum quis blandit. Sed magna purus, ullamcorper quis laoreet sit amet, pretium ac erat. Nam accumsan commodo leo at bibendum. Mauris in mollis ipsum. Etiam lectus nisi, commodo vitae urna at, fermentum lacinia sem. Sed suscipit risus dolor, nec pulvinar tellus porttitor ut. Praesent ullamcorper mattis hendrerit. Praesent euismod leo magna, ac molestie mi egestas nec. Cras suscipit turpis sed erat finibus, ut sodales leo eleifend. Morbi vehicula, orci sit amet consectetur viverra, ex odio pharetra massa, eu porta turpis lacus vel nisi. Cras ac venenatis turpis. Suspendisse consectetur augue nisi, a ornare massa auctor euismod. Nam diam ipsum, hendrerit quis gravida vitae, molestie vitae ante. In dictum sit amet nulla vel gravida.

Morbi vulputate tempor sapien at vulputate. Nulla eget sapien quis lectus fringilla pretium at quis ante. In purus libero, lacinia nec rutrum in, finibus sit amet arcu. Praesent elit odio, luctus non faucibus vitae, eleifend tincidunt urna. Sed lobortis massa in ligula euismod feugiat. Maecenas commodo, mi et posuere sollicitudin, nisl lacus dictum magna, vestibulum euismod arcu est ut elit. Pellentesque ultrices magna enim, id volutpat odio vulputate in. Mauris magna lectus, mattis suscipit ultrices auctor, dapibus vitae dui. Nullam mattis elementum sollicitudin. Fusce viverra tempus odio in hendrerit. Curabitur euismod, lacus nec venenatis porta, velit justo varius justo, quis iaculis enim urna et lacus. Etiam suscipit tempor nisi vitae sagittis. Suspendisse tincidunt, augue non semper convallis, urna arcu facilisis massa, sed elementum ligula dui ac neque.''',
         "description":"this is description of article 5",
         "views":32,
         "likes":16}]

    article_6 = [
         {"content": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eu ligula ut mauris facilisis porta ac in ipsum. Ut pulvinar eget nulla at eleifend. Vivamus euismod urna molestie, convallis ipsum sed, tristique justo. Sed egestas nulla eu tortor blandit, id tempus sem dictum. Vestibulum dictum euismod dolor sed pharetra. Morbi ornare pulvinar metus, eu sagittis ligula hendrerit vel. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras sit amet mollis dui. Etiam dolor sapien, dictum at est eget, aliquam sagittis nibh. Proin eu ex non augue luctus ultrices. Aliquam dictum id tortor aliquet pellentesque. Donec dolor felis, placerat at fermentum in, pharetra nec augue. Aliquam mollis nibh nec nibh iaculis mollis. Curabitur lectus velit, feugiat at sem et, malesuada dictum quam.

Duis lectus magna, vestibulum sed blandit quis, vulputate ac augue. Fusce hendrerit rhoncus viverra. Quisque lacinia nec ipsum quis blandit. Sed magna purus, ullamcorper quis laoreet sit amet, pretium ac erat. Nam accumsan commodo leo at bibendum. Mauris in mollis ipsum. Etiam lectus nisi, commodo vitae urna at, fermentum lacinia sem. Sed suscipit risus dolor, nec pulvinar tellus porttitor ut. Praesent ullamcorper mattis hendrerit. Praesent euismod leo magna, ac molestie mi egestas nec. Cras suscipit turpis sed erat finibus, ut sodales leo eleifend. Morbi vehicula, orci sit amet consectetur viverra, ex odio pharetra massa, eu porta turpis lacus vel nisi. Cras ac venenatis turpis. Suspendisse consectetur augue nisi, a ornare massa auctor euismod. Nam diam ipsum, hendrerit quis gravida vitae, molestie vitae ante. In dictum sit amet nulla vel gravida.

Morbi vulputate tempor sapien at vulputate. Nulla eget sapien quis lectus fringilla pretium at quis ante. In purus libero, lacinia nec rutrum in, finibus sit amet arcu. Praesent elit odio, luctus non faucibus vitae, eleifend tincidunt urna. Sed lobortis massa in ligula euismod feugiat. Maecenas commodo, mi et posuere sollicitudin, nisl lacus dictum magna, vestibulum euismod arcu est ut elit. Pellentesque ultrices magna enim, id volutpat odio vulputate in. Mauris magna lectus, mattis suscipit ultrices auctor, dapibus vitae dui. Nullam mattis elementum sollicitudin. Fusce viverra tempus odio in hendrerit. Curabitur euismod, lacus nec venenatis porta, velit justo varius justo, quis iaculis enim urna et lacus. Etiam suscipit tempor nisi vitae sagittis. Suspendisse tincidunt, augue non semper convallis, urna arcu facilisis massa, sed elementum ligula dui ac neque.''',
         "description":"this is description of article 6",
         "views":9,
         "likes":3}]


    arts = {"Article 1": {"details": article_1},
         "Article 2": {"details": article_2},
         "Article 3": {"details": article_3},
         "Article 4": {"details": article_4},
         "Article 5": {"details": article_5},
         "Article 6": {"details": article_6}, }


    for art, cat_data in arts.items():
        c = add_article(art)
        for d in cat_data["details"]:
            add_details(art, d["content"], d["description"], d["views"], d["likes"])


def add_details(art, content, description, views, likes):
    p = Detail.objects.get_or_create(article=art, description=description)[1]
    p.content = content
    p.views = views
    p.likes = likes
    p.save()
    return p

def add_article(title):
    c = Article.objects.get_or_create(title=title)[0]
    c.save()
    return c



if __name__ == '__main__':
    print("Populating...")
    populate()
