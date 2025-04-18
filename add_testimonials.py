import sys
import os

# Add the neo infra directory to Python path
sys.path.append(os.path.abspath("neo infra"))

from app import create_app
from app.models.testimonial import Testimonial
from datetime import datetime

def add_testimonials():
    app = create_app()
    with app.app_context():
        # Sample testimonials
        testimonials = [
            {
                'quote': 'NEO Infrastructure delivered our project on time and within budget. Their attention to detail and quality of work was exceptional.',
                'name': 'John Smith',
                'company': 'ABC Industries',
                'image_filename': None  # Will use default avatar
            },
            {
                'quote': 'Working with NEO Infrastructure was a great experience. Their team was professional, knowledgeable, and always available to address our concerns.',
                'name': 'Sarah Johnson',
                'company': 'XYZ Corporation',
                'image_filename': None  # Will use default avatar
            },
            {
                'quote': 'The quality of work and commitment to excellence shown by NEO Infrastructure exceeded our expectations. We look forward to future collaborations.',
                'name': 'Michael Brown',
                'company': 'Global Solutions Ltd',
                'image_filename': None  # Will use default avatar
            }
        ]

        # Add testimonials to database
        from app import db
        for testimonial_data in testimonials:
            testimonial = Testimonial(
                quote=testimonial_data['quote'],
                name=testimonial_data['name'],
                company=testimonial_data['company'],
                image_filename=testimonial_data['image_filename'],
                created_at=datetime.utcnow()
            )
            db.session.add(testimonial)

        # Commit changes
        db.session.commit()
        print("Successfully added testimonials to the database!")

if __name__ == '__main__':
    add_testimonials() 