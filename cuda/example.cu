#include <stdio.h>
#include <cuda.h>
#include <time.h>

__global__ void add_vectors(float *a, float *b, float *c, int N) {
  int idx = blockIdx.x * blockDim.x + threadIdx.x;
  if (idx < N) {
    c[idx] = a[idx] + b[idx];
  }
}

int main(void) {
  float *a_h, *a_d, *b_h, *b_d, *c_h, *c_d;
  const int N = 10;
  size_t size = N * sizeof(float);
  a_h = (float *)malloc(size);
  b_h = (float *)malloc(size);
  c_h = (float *)malloc(size);

  srand(time(NULL));

  cudaMalloc((void **) &a_d, size);
  cudaMalloc((void **) &b_d, size);
  cudaMalloc((void **) &c_d, size);

  for (int i=0; i<N; i++) {
    a_h[i] = rand() / (float)RAND_MAX;
    b_h[i] = rand() / (float)RAND_MAX;
  }

  cudaMemcpy(a_d, a_h, size, cudaMemcpyHostToDevice);
  cudaMemcpy(b_d, b_h, size, cudaMemcpyHostToDevice);

  int block_size = 4;
  int n_blocks = N/block_size + (N % block_size == 0 ? 0 : 1);
  add_vectors<<<n_blocks, block_size>>> (a_d, b_d, c_d, N);

  cudaMemcpy(c_h, c_d, sizeof(float)*N, cudaMemcpyDeviceToHost);

  for (int i=0; i<N; i++) {
    printf("%d\t%f\t%f\t= %f\n", i, a_h[i], b_h[i], c_h[i]);
  }

  free(a_h);
  free(b_h);
  free(c_h);
  cudaFree(a_d);
  cudaFree(b_d);
  cudaFree(c_d);
}