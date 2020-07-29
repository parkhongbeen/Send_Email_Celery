from app.example.views import Mailer

mail = Mailer()
mail.send_messages(subject='My App account verification',
                   template='emails/customer_verification.html',
                   context={'customer': self},
                   to_emails=[self.user.email])