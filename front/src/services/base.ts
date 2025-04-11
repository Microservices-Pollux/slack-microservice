export class Base {
  baseUrl: string;
  resource: string;
  parents: string[];

  constructor(resource: string) {
    this.baseUrl = import.meta.env.VITE_API_URL || "http://localhost:5000";
    this.parents = [];
    this.resource = resource;
  }

  getResource(params: any = {}): string {
    let route = this.resource;
    if (this.parents.length > 0) {
      for (let p = 0; p < this.parents.length; p++) {
        route = route.replace(`$${p}`, this.parents[p]);
      }
    }
    if (params.hasOwnProperty("id")) {
      return `${route}/${params.id}`;
    }

    return route;
  }

  get(id?: string, params: any = {}): Promise<any> {
    const url = new URL(`${this.baseUrl}/${this.getResource(params)}`);
    Object.keys(params).forEach((key) => {
      url.searchParams.set(key, params[key]);
    });
    return fetch(url)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => data);
  }

  create(body: any, params: any = {}): Promise<any> {
    const url = new URL(`${this.baseUrl}/${this.getResource(params)}`);
    Object.keys(params).forEach((key) => {
      url.searchParams.set(key, params[key]);
    });
    return fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => data);
  }

  update(id: string, body: any, params: any = {}): Promise<any> {
    const url = new URL(`${this.baseUrl}/${this.getResource(params)}`);
    Object.keys(params).forEach((key) => {
      url.searchParams.set(key, params[key]);
    });
    return fetch(`${url}/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => data);
  }

  delete(id: string, params: any = {}): Promise<any> {
    const url = new URL(`${this.baseUrl}/${this.getResource(params)}`);
    Object.keys(params).forEach((key) => {
      url.searchParams.set(key, params[key]);
    });
    return fetch(`${url}/${id}`, {
      method: "DELETE",
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => data);
  }
}
