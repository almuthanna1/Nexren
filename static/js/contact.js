document.getElementById('contact-form').addEventListener('submit', async e => {
  e.preventDefault();
  const form = e.target;
  const formData = new FormData(form);

  try {
    const res = await fetch('/contact', {
      method: 'POST',
      body: formData
    });

    const result = await res.json();
    if (res.ok) {
      alert('Message sent successfully!');
      form.reset();
    } else {
      alert('Error: ' + result.error);
    }
  } catch (err) {
    alert('Fetch error: ' + err.message);
  }
});
